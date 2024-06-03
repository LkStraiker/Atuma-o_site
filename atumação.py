from playwright.sync_api import sync_playwright
import time


# Função para fazer login
def fazer_login(page):
    print("Iniciando login...")
    # URL da página de login
    url_login = 'https://admin02.imobibrasil.net/imobiliarias/identificacao.php?msg=loginDuplicate'
    page.goto(url_login)
    # Esperar a página de login carregar completamente
    page.wait_for_load_state('networkidle')

    # Preencher formulário de login
    page.fill('input[name="login"]', 'sbliimoveis_1')  # Nome de usuário
    page.fill('input[name="senha"]', 'isabela3')  # Senha

    # Enviar formulário de login e esperar a navegação
    with page.expect_navigation(timeout=60000):
        page.click('input[type="submit"]')

    print("Login concluído.")


# Função para processar os produtos em uma página
def processar_produtos_na_pagina(page):
    # Selecionar todas as caixas de seleção dos produtos
    checkbox_items = page.query_selector_all('.checkbox-item-compartilhar')
    for checkbox in checkbox_items:
        checkbox.click()

    # Clicar no botão "Editar" para abrir a mini página
    page.click('button#btn-editar-em-massa')

    # Esperar a mini página carregar completamente
    page.wait_for_selector('div.content-widget', timeout=60000)

    # Selecionar a tag <select> com id "finalidade"
    select_element = page.query_selector('select#finalidade')

    # Verificar se o elemento foi encontrado
    if select_element:
        # Selecionar a opção "Venda" na select
        page.select_option('select#finalidade', '2')
        print("Opção 'Venda' selecionada.")

        # Adicionar uma pausa para visualização
        time.sleep(2)

        # Clicar no botão "Salvar Todos" para salvar todas as alterações
        page.click('button#btn-confirm-edit')
        print("Alterações salvas.")

        # Esperar pelo desaparecimento do modal swal
        page.wait_for_selector('div.swal2-container', state='detached', timeout=60000)

        # Adicionar uma pausa final para visualização
        time.sleep(2)
    else:
        print("Elemento <select> com id 'finalidade' não encontrado.")


# Função para processar todas as páginas
def processar_produtos(page):
    print("Iniciando processamento de produtos...")

    # Navegar para a seção "CRM Imóveis"
    page.click('span:has-text("CRM Imóveis")')

    # Navegar para "Imóveis: Listar"
    with page.expect_navigation(timeout=60000):
        page.click('a:has-text("Imóveis: Listar")')

    # Preencher o campo de pesquisa com "PS"
    page.fill('input[name="pesquisa"]', 'PS')
    page.press('input[name="pesquisa"]', 'Enter')

    # Esperar a página carregar completamente
    page.wait_for_load_state('networkidle', timeout=60000)
    print("Pesquisa realizada com 'PS'")

    while True:
        # Processar produtos na página atual
        processar_produtos_na_pagina(page)

        # Verificar se existe um botão para a próxima página
        next_page_link = page.query_selector('a.lipagina-btn-paginacao[title="Próxima Página"]')
        if next_page_link:
            # Clicar no botão da próxima página
            with page.expect_navigation():
                next_page_link.click()
            print("Indo para a próxima página...")
            # Adicionar uma pausa para a página carregar
            time.sleep(2)
        else:
            # Se não houver botão para a próxima página, sair do loop
            print("Todas as páginas processadas.")
            break

    print("Processamento de produtos concluído.")


# Função principal
def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    try:
        # Fazer login
        fazer_login(page)
        # Processar os produtos
        processar_produtos(page)
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")
        # Fazer uma captura de tela para entender o que aconteceu
        page.screenshot(path="erro.png")
    finally:
        browser.close()


# Executar o script
with sync_playwright() as playwright:
    run(playwright)
