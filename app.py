import uuid
from pymongo import MongoClient
from flask import Flask 
from flask import request
from flask import jsonify
app = Flask(__name__)
import urllib.parse
from datetime import datetime
from elasticsearch import Elasticsearch

#Conexão com banco ElasticSearch
es = Elasticsearch(
    'meu-favorito-dashboa-543171073.ap-southeast-2.bonsaisearch.net',
    http_auth=('6vi035crgt', 'w8no1zyb2i'),
    scheme="https",
    port=443,
    verify_certs=False 
)

#Conexão com banco MongoDB
username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('44KXC4kr2Jk8r3mV')
client = MongoClient('mongodb://%s:%s@meu-favorito.sv.ufabcnext.com:15003/' % (username, password))
db = client.uberhack

#Rota Inicial
@app.route('/')
def hello():
    Bem vindo a API do Atendente CPFL         


#Endpoint GET para identificar usuario
@app.route('/favorites', methods=['GET','POST'])
def favoritos():
    if request.method == 'GET':
        favoritos = db.favorito
        resultado = []

        for favorito in favoritos.find({"cliente.cliente_empresa_id": request.args.get('cliente')}):
            print(favorito)
            resultado.append(favorito["motorista"])

        return jsonify(favoritos=resultado) 
    
        
    if request.method == 'POST':
        req = request.json
        motoristas = db.motorista
        motorista = motoristas.find_one({"motorista_empresa_id":req['motorista_empresa_id']})

        if motorista == None:   
            motorista = { 
                "_id" : uuid.uuid4().hex,
                "nome" : req['nome_motorista'],
                "foto" : req['foto'],
                "motorista_empresa_id" : req['motorista_empresa_id'],
                "empresa" : req['empresa'], 
                "data_insercao" : datetime.now().isoformat()
            }
            motorista["mongo_id"] = motorista["_id"] 
            motoristas.insert_one(motorista)
            del motorista["_id"]
            es.index(index="motorista", doc_type='doc_motorista', id=uuid.uuid4().hex, body=motorista)

        clientes = db.cliente
        cliente = clientes.find_one({"cliente_empresa_id":req['cliente_empresa_id']})

        if cliente == None:
            cliente = {
                "_id" : uuid.uuid4().hex,
                "nome" : req['nome_cliente'],
                "cliente_empresa_id" : req['cliente_empresa_id'],
                "empresa" : req['empresa'],
                "data_insercao" : datetime.now().isoformat()
            }
            cliente["mongo_id"] = cliente["_id"] 
            clientes.insert_one(cliente)
            del cliente["_id"]
            es.index(index="cliente", doc_type='doc_cliente', id=uuid.uuid4().hex, body=cliente)

        favorito = {
            "_id" : uuid.uuid4().hex,
            "motorista" : motorista,
            "cliente" : cliente,
            "empresa" : req['empresa'],
            "data_insercao" : datetime.now().isoformat()
        }

        favoritos = db.favorito
        favorito["mongo_id"] = favorito["_id"] 
        favoritos.insert_one(favorito)
        del favorito["_id"]
        es.index(index="favorito", doc_type='doc_favorito', id=uuid.uuid4().hex, body=favorito)

    return jsonify(menssagem={"sucesso":"true"}) 


if __name__ == '__main__':
    app.run(debug=True)