# Agenda Telefônica — Django

Aplicação web de agenda telefônica (CRUD de contatos) desenvolvida em Django. Este documento explica como configurar e executar o projeto localmente no **Windows** e no **Linux**.

Veja também o [README principal do repositório](../README.md).

## Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/)
- `pip` (já vem junto com o Python)

Verifique a versão instalada:

```bash
python --version
```

> No Linux, o executável costuma se chamar `python3` em vez de `python`.

## 1. Clonar o repositório

```bash
git clone https://github.com/orlandosaraivajr/Seccomp-Rio-Claro-2026
cd Seccomp-Rio-Claro-2026/src
```

## 2. Criar e ativar o ambiente virtual

Um ambiente virtual isola as dependências do projeto do resto do sistema.

### Windows (PowerShell)

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

Se aparecer um erro de política de execução de scripts, rode o comando abaixo (uma vez, apenas na sessão atual do PowerShell) e tente ativar novamente:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### Windows (CMD)

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

### Linux / macOS (bash/zsh)

```bash
python3 -m venv venv
source venv/bin/activate
```

Em todos os casos, o terminal passa a exibir `(venv)` no início da linha, indicando que o ambiente virtual está ativo.

## 3. Instalar as dependências

Com o ambiente virtual ativado:

```bash
pip install -r requirements.txt
```

## 4. Aplicar as migrations (criar o banco de dados)

```bash
python manage.py migrate
```

## 5. (Opcional) Criar um super usuário

Necessário apenas para acessar o painel administrativo em `/admin/`.

```bash
python manage.py createsuperuser
```

## 6. Executar o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse no navegador: **http://127.0.0.1:8000/**

## 7. Executar os testes automatizados

```bash
python manage.py test contatos
```

## Comandos úteis (resumo)

| Ação | Windows (PowerShell) | Linux / macOS |
|---|---|---|
| Criar venv | `python -m venv venv` | `python3 -m venv venv` |
| Ativar venv | `venv\Scripts\Activate.ps1` | `source venv/bin/activate` |
| Desativar venv | `deactivate` | `deactivate` |
| Instalar dependências | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Rodar migrations | `python manage.py migrate` | `python manage.py migrate` |
| Subir servidor | `python manage.py runserver` | `python manage.py runserver` |
| Rodar testes | `python manage.py test contatos` | `python manage.py test contatos` |

## Estrutura do projeto

```
src/
├── manage.py
├── requirements.txt
├── agenda_telefonica/   # configurações do projeto Django (settings, urls)
└── contatos/            # app com o CRUD de contatos (models, views, forms, templates, tests)
```
