from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>hello, world</p>"

  #exemplo de um dicionario para simular um "banco de dados"
banco_de_dados = {}

@app.route('/adicionar_dados', methods=['POST'])
def adicionar_dados():
  dados = requests.get_json()

  #verificar se requisicao possui o campo 'chave' e 'valor'
  if 'chave' in dados and 'valor' in dados:
    chave = dados['chave']
    valor = dados['valor']

    #adicionar os dados ao banco de dados simulado
    banco_de_dados[chave] = valor

    return jsonify({'<p>mensagem': 'Dados adicionado com sucesso!</p>'})

  return jsonify({'<p>erro': 'Campo "chave" e "valor" sao obrigatorio</p>'}), 400

if __name__=='__main__':
  app.run(debug=True)