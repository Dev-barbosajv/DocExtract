# Projeto de Extração de Dados de PDF para CSV 

Este projeto consiste em uma aplicação web desenvolvida em Python utilizando o framework Flask. A principal funcionalidade da aplicação é extrair dados de arquivos PDF e exportá-los para um arquivo CSV.

## Como Funciona

1. **Upload do Arquivo PDF**: O usuário faz o upload de um arquivo PDF contendo dados a serem extraídos.
2. **Extração dos Dados**: Os dados são extraídos do arquivo PDF utilizando expressões regulares.
3. **Visualização dos Dados**: Os dados extraídos são exibidos na interface web para que o usuário possa revisá-los.
4. **Exportação para CSV**: O usuário pode exportar os dados visualizados para um arquivo CSV.
5. **Limpeza de Dados**: Os dados são removidos da sessão após a exportação para garantir a privacidade.

## Pré-Requisitos

Certifique-se de ter Python instalado em seu ambiente. Caso contrário, você pode baixá-lo [aqui](https://www.python.org/downloads/).

## Instalação

1. Clone o repositório do projeto:

    ```
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    ```

2. Instale as dependências do projeto:

    ```
    pip install -r requirements.txt
    ```

## Executando a Aplicação

1. Navegue até o diretório do projeto:

    ```
    cd nome-do-repositorio
    ```

2. Execute o arquivo `app.py`:

    ```
    python app.py
    ```

3. Acesse a aplicação em seu navegador web em [http://localhost:5000/](http://localhost:5000/).

## Como Usar

1. Na página inicial, clique no botão "Escolher Arquivo" para fazer o upload de um arquivo PDF.
2. Após selecionar o arquivo, clique no botão "Extrair Informações".
3. Os dados extraídos serão exibidos na página.
4. Para exportar os dados para um arquivo CSV, clique no botão "Exportar para CSV".
5. O arquivo CSV será baixado automaticamente.

## Observações

- Certifique-se de que o arquivo PDF contém os dados no formato esperado para uma extração correta.
- A aplicação está configurada para rodar em modo de depuração (`debug=True`). Para ambientes de produção, desative esse modo e configure as variáveis de ambiente apropriadas.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## Licença

Este projeto está licenciado sob a licença [MIT](https://github.com/seu-usuario/nome-do-repositorio/blob/main/LICENSE).
