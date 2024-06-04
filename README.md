Imobiliária Automação de Processamento de Produtos
Este script automatiza o processo de login e edição em massa de produtos em um sistema de gerenciamento imobiliário. Utiliza a biblioteca Playwright para realizar ações automatizadas no navegador.

Funcionalidades
Login automático no sistema imobiliário.
Pesquisa de produtos com o termo "PS".
Seleção de todos os produtos listados.
Edição em massa para definir a finalidade como "Venda".
Salvamento das alterações realizadas.
Navegação automática entre as páginas de resultados.
Requisitos
Python 3.7 ou superior
Playwright
Instalação
Clone este repositório:

sh
Copiar código
git clone https://github.com/seu-usuario/imobiliaria-automacao.git
cd imobiliaria-automacao
Crie e ative um ambiente virtual (opcional, mas recomendado):

sh
Copiar código
python -m venv venv
source venv/bin/activate  # Para Windows, use `venv\Scripts\activate`
Instale as dependências:

sh
Copiar código
pip install playwright
playwright install
Uso
Edite o script main.py para inserir suas credenciais de login:

python
Copiar código
# No método fazer_login
page.fill('input[name="login"]', 'seu_usuario')  # Nome de usuário
page.fill('input[name="senha"]', 'sua_senha')    # Senha
Execute o script:

sh
Copiar código
python main.py
O script abrirá um navegador, fará login no sistema, realizará a pesquisa, editará os produtos em massa e navegará automaticamente entre as páginas até que todos os produtos sejam processados.

Estrutura do Código
fazer_login(page): Realiza o login no sistema.
processar_produtos_na_pagina(page): Processa todos os produtos na página atual.
processar_produtos(page): Realiza a pesquisa e gerencia a navegação entre as páginas de resultados.
run(playwright): Função principal que inicia o navegador, faz login e inicia o processamento dos produtos.
Solução de Problemas
Caso ocorra algum erro, uma captura de tela será salva com o nome erro.png na pasta do projeto.
Verifique se as credenciais de login estão corretas e se a página inicial está acessível.
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

Se precisar de mais informações ou alterações, sinta-se à vontade para me avisar!
