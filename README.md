# Sistema de Controle de Tarefas e Registro de Tempo

Este projeto é um sistema de controle de tarefas e registro de tempo, desenvolvido com Django como parte de um desafio técnico. Ele permite o cadastro de tarefas e registros de tempo associados a essas tarefas, além de listagens com filtros.

## Funcionalidades

- Cadastro de tarefas (com nome do usuário responsável, descrição e data de criação).
- Registro de tempo de trabalho (com data, quantidade de horas, descrição do trabalho e relação com uma tarefa).
- Listagem de tarefas e registros com filtros avançados.

## Requisitos

Certifique-se de que você tem os seguintes itens instalados em sua máquina:

- [Python 3.x](https://www.python.org/downloads/)

## Configuração do Projeto

### 1. Clone o Repositório

Clone o projeto do GitHub ou baixe-o diretamente.

```bash
git clone https://github.com/kauansb/desafio_tarefas.git
cd desafio_tarefas
```

Configure um ambiente virtual isolado e o ative (OPCIONAL!)
```bash
python -m venv venv 
source venv/bin/activate  # No Windows: venv\Scripts\activate

```

Instale as dependências do projeto
```bash
pip install -r requirements.txt

```

Aplicar as Migrações
```bash
python manage.py migrate

```

Criar um Superusuário para acessar o painel administrativo do Django
```bash
python manage.py createsuperuser

```


Rodar o Servidor Localmente
```bash
python manage.py runserver

```

Acesse o projeto no navegador em http://127.0.0.1:8000.
