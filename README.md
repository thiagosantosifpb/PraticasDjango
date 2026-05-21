# Práticas Django — Práticas 01 a 09

Projeto desenvolvido para a disciplina **Desenvolvimento Ágil com Ferramenta RAD**, reunindo as práticas de Django em uma aplicação simples para gerenciamento de livros.

## Práticas contempladas

- **Prática 01**: preparação do ambiente com Docker e criação do projeto Django.
- **Prática 02**: criação do app `blog`, rotas e views.
- **Prática 03**: uso de templates com variáveis, condicionais, loops, URL tag e herança.
- **Prática 04**: criação dos modelos com Django ORM e migrations.
- **Prática 05**: implementação de CRUDs completos usando `ModelForm`.
- **Prática 06**: paginação, geração de dados com Faker e comando customizado.
- **Prática 07**: autenticação com cadastro, login, logout e rotas protegidas.
- **Prática 08**: autorização com grupo e permissões para gerenciamento de livros.

---

## Visão geral do sistema

O app `edu` implementa um sistema de cadastro de:

- **Autores**
- **Editoras**
- **Livros**
- **Publicações**, que representam a relação entre Livro e Autor

O sistema possui listagem paginada, formulários dinâmicos, cadastro de usuários, autenticação e controle de autorização para ações sensíveis.

---

## Funcionalidades implementadas

### CRUD com ModelForm

Foram criados formulários baseados em `ModelForm` para os modelos:

- `AutorForm`
- `EditoraForm`
- `LivroForm`
- `PublicaForm`

Cada entidade possui rotas para:

- listar registros;
- cadastrar novo registro;
- editar registro existente;
- excluir registro.

Arquivos principais:

```text
edu/forms.py
edu/views.py
edu/urls.py
edu/templates/edu/
```

---

### Autenticação

A aplicação possui:

- cadastro de usuários;
- login;
- logout;
- exibição do nome do usuário logado na interface;
- proteção de rotas de criação, edição e exclusão.

Rotas principais:

```text
/accounts/signup/   -> cadastro de usuário
/accounts/login/    -> login
/accounts/logout/   -> logout, via POST pelo botão Sair
```

---

### Autorização para gerenciamento de livros

As ações de gerenciamento de livros exigem permissões específicas do Django:

```text
edu.add_livro       -> cadastrar livros
edu.change_livro    -> editar livros
edu.delete_livro    -> excluir livros
```

Usuários sem essas permissões conseguem visualizar a lista, mas não conseguem cadastrar, editar ou remover livros.

O grupo utilizado para essa regra é:

```text
Analistas de cadastro de produtos
```

O projeto inclui um comando para criar ou atualizar esse grupo automaticamente.

---

## Fluxo de execução do sistema

### 1. Subir os containers

```bash
docker compose up -d --build
```

### 2. Executar as migrations

```bash
docker compose exec web python manage.py migrate
```

### 3. Criar um superusuário

```bash
docker compose exec web python manage.py createsuperuser
```

Esse usuário será usado para acessar o Django Admin.

### 4. Criar o grupo de analistas

```bash
docker compose exec web python manage.py criar_grupo_analistas
```

Esse comando cria o grupo **Analistas de cadastro de produtos** e adiciona as permissões de visualizar, cadastrar, editar e excluir livros.

### 5. Acessar o Admin

Abra no navegador:

```text
http://localhost:8000/admin/
```

No Admin, crie ou edite usuários e adicione ao grupo **Analistas de cadastro de produtos** aqueles que poderão gerenciar livros.

### 6. Gerar dados de teste, opcional

```bash
docker compose exec web python manage.py gerar_livros
```

Também é possível informar uma quantidade específica:

```bash
docker compose exec web python manage.py gerar_livros --quantidade 30
```

### 7. Acessar a aplicação

```text
http://localhost:8000/livros/
```

A partir dessa tela, é possível navegar entre livros, autores, editoras e publicações.

---

## Fluxo de uso recomendado para teste

### Teste 1 — Usuário não logado

1. Acesse `http://localhost:8000/livros/`.
2. Verifique que a listagem aparece normalmente.
3. Tente acessar `http://localhost:8000/livros/novo/`.
4. O sistema deve redirecionar para a tela de login.

### Teste 2 — Usuário logado sem permissão

1. Cadastre um usuário comum em `http://localhost:8000/accounts/signup/`.
2. Faça login com esse usuário.
3. Acesse a listagem de livros.
4. Verifique que as opções de cadastrar, editar e excluir livros não aparecem.
5. Caso tente acessar diretamente uma rota protegida de livros, o sistema negará a ação.

### Teste 3 — Usuário analista com permissão

1. Acesse o Admin com o superusuário.
2. Adicione o usuário desejado ao grupo **Analistas de cadastro de produtos**.
3. Faça login na aplicação com esse usuário.
4. Acesse `http://localhost:8000/livros/`.
5. Verifique que as opções de cadastrar, editar e excluir livros estão disponíveis.

---

## Rotas principais

### Edu

```text
/livros/
/livros/novo/
/livros/<id>/editar/
/livros/<id>/excluir/

/autores/
/autores/novo/
/autores/<id>/editar/
/autores/<id>/excluir/

/editoras/
/editoras/novo/
/editoras/<id>/editar/
/editoras/<id>/excluir/

/publicacoes/
/publicacoes/novo/
/publicacoes/<id>/editar/
/publicacoes/<id>/excluir/
```

### Autenticação

```text
/accounts/signup/
/accounts/login/
/accounts/logout/
```

### Admin

```text
/admin/
```

### Blog

```text
/
/contato/83999990000/
/blog/welcome/
/blog/eco/ola/
/blog/info/
```

---

## Estrutura principal

```text
manage.py
requirements.txt
Dockerfile
docker-compose.yaml

myapp/
 ├── settings.py
 ├── urls.py
 ├── asgi.py
 └── wsgi.py

blog/
 ├── views.py
 ├── urls.py
 └── templates/

edu/
 ├── admin.py
 ├── forms.py
 ├── models.py
 ├── urls.py
 ├── views.py
 ├── templates/
 │   ├── edu/
 │   │   ├── base.html
 │   │   ├── lista_generica.html
 │   │   ├── lista_livros.html
 │   │   ├── form_generico.html
 │   │   ├── confirmar_exclusao.html
 │   │   └── signup.html
 │   └── registration/
 │       └── login.html
 └── management/
     └── commands/
         ├── gerar_livros.py
         └── criar_grupo_analistas.py
```

---

## Tecnologias utilizadas

- Python 3.12
- Django
- SQLite
- Faker
- Docker
- Docker Compose

---

## Observações importantes

- O logout do Django é executado por método `POST`, por isso a interface possui um botão **Sair** dentro de um formulário.
- As rotas de gerenciamento de livros usam as permissões nativas do Django.
- O grupo de analistas pode ser criado manualmente pelo Admin ou automaticamente pelo comando `criar_grupo_analistas`.
- Para cadastrar um livro, é necessário já existir ao menos uma editora cadastrada.
- Para cadastrar uma publicação, é necessário já existir ao menos um livro e um autor cadastrados.

## Prática 09 - API REST com Django REST Framework

Nesta prática foi adicionada uma API RESTful usando Django REST Framework.

### Recursos disponíveis na API

- Autor
- Editora

### Endpoints

| Recurso | Método | URL | Descrição |
|---|---|---|---|
| Autores | GET | `/api/autores/` | Lista autores |
| Autores | POST | `/api/autores/` | Cria autor |
| Autor | GET | `/api/autores/<id>/` | Detalha autor |
| Autor | PUT/PATCH | `/api/autores/<id>/` | Atualiza autor |
| Autor | DELETE | `/api/autores/<id>/` | Remove autor |
| Editoras | GET | `/api/editoras/` | Lista editoras |
| Editoras | POST | `/api/editoras/` | Cria editora |
| Editora | GET | `/api/editoras/<id>/` | Detalha editora |
| Editora | PUT/PATCH | `/api/editoras/<id>/` | Atualiza editora |
| Editora | DELETE | `/api/editoras/<id>/` | Remove editora |

### Executando

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
