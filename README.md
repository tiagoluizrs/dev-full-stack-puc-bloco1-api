# API RESTful para site de vídeos e séries

## Descrição
Está API tem como objetivo permitir que um usuário crie uma conta, realize login, liste e crie filmes e séries e possa avaliar esses filmes e séries.

## Manual de instalação
Versão do Python utilizada: 3.12.4 (Qualquer versão diferente pode gerar problemas para a configuração do ambiente)

Para instalar as dependências  é recomendável mas não obrigatório o uso de um ambiente virtual. Para criar um ambiente virtual, execute o seguinte comando:

> Uma exigência para instalar as dependências é que será necessário estar na pasta raiz do projeto e rodar 

```bash
pip install -r requirements.txt
```

Após isso todas as libs serão instaladas e para rodar a API rode o comando

```bash
flask --app app run --debug
```

Após rodar, sua API estará disponível na porta 5000 através da url http://127.0.0.1:5000 e para acessar o Swagger da API, acesse a url: http://127.0.0.1:5000/apidocs/

> **Atenção:** Para testar a API através do swagger você precisará antes criar um usuário e realizar login com ele, pois a API exige um token JWT que deve ser enviado no cabeçalho das requisições. Apenas os ENDPOINTS de registro e login são públicos, os demais exigem esse token, então crie um usuário e realize login e você receberá o token na resposta da requisição de login. Esse post tem duração de 3 horas, caso contrário você precisará realizar novamente login para pegar um novo token.

Referências:
- [Flask](https://flask.palletsprojects.com/en/2.3.x/)
- [Livro Flask de A a Z](https://www.casadocodigo.com.br/products/livro-flask-a-z) (Livro de minha autoria publicado pela Casa do Código)