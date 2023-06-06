# Blog Pessoal

Este é um aplicativo web simples de blog pessoal construído com Django.

## Pré-requisitos

Certifique-se de ter o seguinte instalado:

- Python (versão 3.7 ou superior)
- Django (versão 3.2 ou superior)

## Primeiros Passos

1. Clone o repositório:

   `<repository_url>`

2. Navegue até o diretório do projeto:

   `cd personalblog`

3. Instale as dependências necessárias:

   `pip install -r requirements.txt`

4. Inicialize o banco de dados:

   `python manage.py migrate`

5. Crie uma conta de superusuário (para acesso de administrador):

   `python manage.py createsuperuser`

6. Execute o servidor de desenvolvimento:

   `python manage.py runserver`

7. Acesse o blog em seu navegador da web:

   `http://localhost:8000/posts/`

8. Faça login com sua conta de superusuário em:

   `http://localhost:8000/admin/`

## Uso

- Para criar uma nova postagem no blog, faça login como usuário com privilégios de administrador e clique em "Criar Postagem" na interface de administração ou acesse `http://localhost:8000/posts/create/`.
- Apenas usuários logados podem criar postagens. Outros visitantes podem visualizar a lista de postagens e ler postagens individuais.
- Você pode personalizar os templates, adicionar recursos e fazer outras modificações para atender às suas necessidades.

## Estrutura de Pastas

A estrutura de pastas do projeto é a seguinte:

├── blog
│ ├── migrations
│ ├── static
│ ├── templates
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ └── views.py
├── personalblog
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
└── README.md


- A pasta `blog` contém o aplicativo Django para o blog, incluindo modelos, visualizações, templates e formulários.
- A pasta `personalblog` contém os arquivos de configuração do projeto em nível de configuração, incluindo configurações e URLs.
- O arquivo `manage.py` é usado para vários comandos de gerenciamento.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
