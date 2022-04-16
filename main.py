

from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/')
def homePage():
  tabela = pd.read_csv('tabela.csv')
  tabelaId = tabela['id']
  tabelaTitle = tabela['title']
  tabelaAutor = tabela['title']
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