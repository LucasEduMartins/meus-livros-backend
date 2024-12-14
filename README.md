# 📚 API de Cadastro de Livros e Comentários

Esta é uma API desenvolvida em Python utilizando o framework Flask. Ela permite cadastrar livros e adicionar comentários relacionados a cada livro.

## 🚀 Funcionalidades

- **Cadastrar Livros**: Adicione livros com informações básicas como título e autor.
- **Listar Livros**: Consulte todos os livros cadastrados.
- **Adicionar Comentários**: Associe comentários a livros específicos.
- **Listar Comentários**: Consulte todos os comentários relacionados a um livro.
- **Excluir Livros e Comentários**: Remova livros ou comentários da base de dados.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Flask**
- **Flask-SQLAlchemy** (para banco de dados)
- **SQLite** (ou outro banco de dados relacional à sua escolha)

---

## ▶️ Como Rodar o Projeto

### Pré-requisitos

- **Python 3.x** instalado na máquina.
- Gerenciador de pacotes `pip` (instalado junto com Python).

### Passos

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/api-livros.git
cd api-livros
```

2. Crie um ambiente virtual e ative-o:

```bash
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação:

```bash
python app.py
```

A API estará disponível em http://127.0.0.1:5000.

## 📦 Documentação da API

Para obter informações detalhadas sobre os endpoints e como utilizar a API, consulte a [Documentação da API](http://127.0.0.1:5000/openapi/swagger#).

:::note
Certifique-se de ter a aplicação rodando para acessar a documentação da API.
:::
