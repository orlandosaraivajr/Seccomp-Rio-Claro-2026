# Seccomp Rio Claro 2026 — Agenda Telefônica

Projeto de exemplo desenvolvido para a apresentação no **Seccomp Rio Claro 2026**, demonstrando a construção de uma aplicação web completa (CRUD) em Django com o auxílio de um assistente de IA.

A aplicação é uma **agenda telefônica** onde é possível cadastrar contatos com nome, telefone e categoria (Amigos ou Família), com uma interface inspirada no Google Agenda.

## Vídeo da apresentação

📺 Assista à apresentação completa no YouTube: **[https://youtu.be/9iBN4aiDlok](https://youtu.be/9iBN4aiDlok)**

## Estrutura do repositório

- **[src/](src/)** — código-fonte do projeto Django (agenda telefônica). Veja o [README](src/README.md) dentro da pasta para instruções detalhadas de instalação e execução em **Windows** e **Linux**.
- `Seccomp_2026_Unesp.pdf` / `Seccomp_2026_Unesp.odp` — slides utilizados na apresentação.

## Funcionalidades

- Cadastro, listagem, edição e exclusão de contatos (CRUD completo)
- Campos: Nome, Telefone e Categoria (combobox: Amigos / Família)
- Busca de contatos por nome
- Filtro de contatos por categoria
- Painel administrativo do Django (`/admin/`)
- Testes unitários cobrindo todas as rotas

## Tecnologias

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- SQLite (banco de dados padrão de desenvolvimento)

## Como executar

As instruções completas de instalação e execução (Windows e Linux) estão no [README.md do diretório src](src/README.md).

## Autor

Orlando Saraiva Jr.
