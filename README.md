# Práticas Django — Práticas 01, 02, 03, 04 e 06

Este projeto reúne, em sequência, o que foi solicitado nas práticas:

* **Prática 01**: preparação do ambiente com Docker e criação do projeto Django.
* **Prática 02**: criação do app `blog`, rotas e views.
* **Prática 03**: uso de templates com variáveis, condicionais, loops, URL tag e herança.
* **Prática 04**: entendimento dos conceitos de Model, Migration e uso do ORM do Django.
* **Prática 06**: paginação de dados, geração de dados com Faker e criação de comandos customizados do Django.

---

# App `edu`

O app `edu` implementa um sistema de cadastro de:

* Autores
* Editoras
* Livros
* Publicações (relação Livro × Autor)

## Funcionalidades

* Relacionamentos com `ForeignKey`
* Restrições de unicidade (ISBN, nome, etc.)
* Registro no Django Admin
* Paginação de livros (10 por página)
* Comando customizado para geração de dados fake

---

# Paginação

A listagem de livros foi implementada com `Paginator` do Django:

* 10 livros por página
* Navegação entre páginas
* Acesso direto a qualquer página
* Botões anterior e próximo

---

# Comando Faker

Foi criado um **Base Command** para gerar 100 livros automaticamente:

```bash
python manage.py gerar_livros
```

O comando utiliza:

* Faker ISBN provider
* Faker Lorem
* Faker Date Time
* Valores aleatórios de preço e estoque

---

# Como executar

```bash
docker compose up -d --build
docker compose exec web python manage.py migrate
docker compose up
```

---

# Rotas principais

## Blog

* http://localhost:8000/
* http://localhost:8000/contato/83999990000/
* http://localhost:8000/blog/welcome/
* http://localhost:8000/blog/eco/ola/
* http://localhost:8000/blog/info/

## Edu

* http://localhost:8000/livros/
* http://localhost:8000/admin/

---

# Estrutura principal

```
manage.py
requirements.txt

myapp/
blog/
edu/

edu/
 ├── models.py
 ├── admin.py
 ├── views.py
 ├── urls.py
 ├── templates/
 └── management/
     └── commands/
         └── gerar_livros.py
```

---

# Admin Django

O admin possui:

* Paginação de 10 registros
* Filtros
* Busca
* Ordenação

Acesso:

```
http://localhost:8000/admin/
```

---

# Tecnologias utilizadas

* Django
* SQLite
* Faker
* Docker
* Python 3.12
