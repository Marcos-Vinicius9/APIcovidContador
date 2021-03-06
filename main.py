

from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def homePage():
  return 'Api funcionando.'

  
@app.route('/dados')
def dataPage():
  tabela = pd.read_csv('tabela.csv')
  tabelaAutor = tabela['autor']
  tabelaTitle = tabela['title']
  tabelaId = tabela['id']
  tabelaLink= tabela['link']

  respostas = []
  
  for i in range(len(tabela)):
    respostas.append ({
      'id': tabelaId[i], 
      'title': tabelaTitle[i], 
      'autor': tabelaAutor[i], 
      'link': tabelaLink[i]})
    
  return jsonify(respostas)

app.run(host='0.0.0.0')