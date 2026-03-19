# Projeto Django - Práticas 01, 02 e 03

Este projeto reúne, em sequência, o que foi solicitado nas três práticas:

- **Prática 01**: preparação do ambiente com Docker e criação do projeto Django.
- **Prática 02**: criação do app `blog`, rotas e views.
- **Prática 03**: uso de templates com variáveis, condicionais, loops, URL tag e herança.

## Como executar

```bash
docker compose up -d --build
docker compose exec web python manage.py migrate
docker compose up
```

## Rotas principais

- `http://localhost:8000/`
- `http://localhost:8000/contato/83999990000/`
- `http://localhost:8000/blog/welcome/`
- `http://localhost:8000/blog/eco/ola/`
- `http://localhost:8000/blog/info/`

## Estrutura principal

- `Dockerfile`
- `docker-compose.yaml`
- `requirements.txt`
- `manage.py`
- `myapp/`
- `blog/`
- `blog/templates/blog/`
