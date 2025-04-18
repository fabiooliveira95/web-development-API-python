# 🌐 Web Development API em Python

Este projeto tem como objetivo desenvolver uma API RESTful simples utilizando **Python** e o framework **Flask**. A aplicação simula operações básicas de uma API para manipulação de dados via requisições HTTP.

---

## 🚀 Funcionalidades

- ✅ Criar dados via `POST`
- 📄 Listar todos os dados com `GET`
- 🔍 Buscar dados por ID com `GET`
- ✏️ Atualizar dados com `PUT`
- ❌ Remover dados com `DELETE`

---

## 🛠️ Tecnologias Utilizadas

- Python 3.11
- Flask
- JSON (como formato de entrada/saída)
- Postman (para testes de endpoints)

---

## 📦 Instalação e Execução

1. Clone o repositório:

```bash
   git clone https://github.com/fabiooliveira95/web-development-API-python.git
```

```bash
   cd web-development-API-python
```

2.(Recomendada) Crie um ambiente virtual:
```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
```
3.Instale as dependências: 
```bash
   pip install flask
```
4.Execute a aplicação:

```bash
   python app.py
```

## 🔁 Endpoints da API

| Método   | Rota           | Descrição                       |
|----------|----------------|----------------------------------|
| GET      | `/dados`       | Retorna todos os registros       |
| GET      | `/dados/<id>`  | Retorna um registro específico   |
| POST     | `/dados`       | Cria um novo registro            |
| PUT      | `/dados/<id>`  | Atualiza um registro existente   |
| DELETE   | `/dados/<id>`  | Remove um registro               |


## 📬 Contato

Fábio Oliveira
🔗 [LinkedIn](https://www.linkedin.com/in/fabio-oliveira-araujo-cientista/)
📧 fabiooliveira0067@gmail.com
