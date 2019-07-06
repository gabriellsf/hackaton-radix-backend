import uuid
from pymongo import MongoClient
from flask import Flask 
from flask import request
from flask import jsonify
app = Flask(__name__)
import urllib.parse
from datetime import datetime
from elasticsearch import Elasticsearch
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.response_selection import get_first_response


#Conexão com banco ElasticSearch
es = Elasticsearch(
    'cluster-gabs-7913461332.us-west-2.bonsaisearch.net',
    http_auth=('wayhnmmp6q', 'oqoibzr07b'),
    scheme="https",
    port=443,
    verify_certs=False 
)

#Conexão com banco MongoDB
username = urllib.parse.quote_plus('gabs')
password = urllib.parse.quote_plus('admin')
client = MongoClient('mongodb://%s:%s@cluster0-dp1ye.mongodb.net/test?retryWrites=true&w=majority' % (username, password))
db = client.cpfl

bot = ChatBot('CPFL ChatBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.70,
            'response_selection_method': get_first_response
        }
    ]
)

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 
        'Você gosta de programar?', 'Sim, eu programo em Python']

trainer = ListTrainer(bot)
trainer.train(conversa)

#Rota Inicial
@app.route('/')
def hello():
    response = bot.get_response('Oi')
    print(response)

    return "Bem vindo a API do Atendente CPFL"


#Endpoint GET para identificar usuario
#Endpoint POST para conversa
@app.route('/chat', methods=['GET','POST'])
def chat():
    if request.method == 'GET':
        clienteCol = db.cliente
        cliente = clienteCol.find({"_id": request.args.get('id')})
        
        sessao = {
            "_id" : uuid.uuid4().hex,
            "cliente": cliente,
            "data_insercao" : datetime.now().isoformat()
        }
        sessaoCol = db.sessao
        sessaoCol.insert_one(sessao)
        sessao = prepareMongoToEs(sessao)
        es.index(index="sessao", doc_type='doc_sessao', id=uuid.uuid4().hex, body=sessao)

        return jsonify(cliente=cliente) 
        
    if request.method == 'POST':
        req = request.json
        resp = bot.get_response(req['resposta'])
        print(resp)
        return jsonify(menssagem={"sucesso":"true"}) 

def prepareMongoToEs(data):
    data["mongo_id"] = data["_id"]
    del data["_id"]
    return data

if __name__ == '__main__':
    app.run(debug=True)