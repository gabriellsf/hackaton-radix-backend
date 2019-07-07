import configWorkspace
import uuid
import base64
import requests
import json
from pymongo import MongoClient
from flask import Flask 
from flask_cors import CORS
from flask import request
from flask import jsonify
app = Flask(__name__)
import urllib.parse
from datetime import datetime
from elasticsearch import Elasticsearch
from ibm_watson import AssistantV1

CORS(app)
API_FACES_ENDPOINT = 'https://radixhack.cognitiveservices.azure.com/face/v1.0/'
detectUrl = API_FACES_ENDPOINT+"/detect"
verifyUrl = API_FACES_ENDPOINT+"/verify"
FACES_KEY = '9a7ff2d4826646de85ffc1fbbb6fba5b'

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
client = MongoClient('mongodb+srv://%s:%s@cluster0-dp1ye.mongodb.net/test?retryWrites=true&w=majority' % (username, password))
db = client.cpfl

assistant = AssistantV1(
    version='2019-07-07',
    iam_apikey='amF01PbQcjLXKTbOodjJ3wDLJBcdNS2mRKHaaQqELsfE',
    url='https://gateway.watsonplatform.net/assistant/api'
)
assistant.set_http_config({'timeout': 100})

#workspace = assistant.create_workspace(
    #name=configWorkspace.data['name'],
    #description=configWorkspace.data['description'],
    #language=configWorkspace.data['language'],
    #intents=configWorkspace.data['intents'],
    #entities=configWorkspace.data['entities'],
    #counterexamples=configWorkspace.data['counterexamples'],
    #metadata=configWorkspace.data['metadata']
#).get_result()

workspace = assistant.get_workspace(workspace_id="0f156808-de0f-4c7c-a97f-408808cabe79").get_result()
workspace_id = workspace['workspace_id']
#workspace = assistant.get_workspace(workspace_id=workspace_id).get_result()

#Rota Inicial
@app.route('/')
def hello():
    return "Bem vindo a API do Atendente CPFL"


#Endpoint GET para identificar usuario
#Endpoint POST para conversa
@app.route('/chat', methods=['GET','POST'])
def chat():
    if request.method == 'GET':
        clienteCol = db.cliente
        cliente = clienteCol.find_one({"_id": request.args.get('id')})
        
        sessao = {
            "_id" : uuid.uuid4().hex,
            "cliente": cliente,
            "data_insercao" : datetime.now().isoformat()
        }

        sessaoCol = db.sessao
        sessaoCol.insert_one(sessao)
        sessao = prepareMongoToEs(sessao)
        es.index(index="sessao", doc_type='doc_sessao', id=uuid.uuid4().hex, body=sessao)

        response = assistant.message(
            workspace_id=workspace_id,
            input={
               'text': 'Olá'
            },
            context={
               cliente['perfil'] : True
            }
        ).get_result()
        
        return jsonify(cliente=cliente, resposta=response["output"]["text"], context=response["context"]) 
        
    if request.method == 'POST':
        req = request.json        
        response = assistant.message(
            workspace_id=workspace_id,
            input={
               'text': req["text"]
            },
            context= req["context"]
        ).get_result()

        if req['foto'] != None and req['foto'] != "":
            sucesso = "Sim" 
            decoded = base64.decodebytes(req['foto'])
            headers = {
                "Content-Type" : "application/octet-stream",
                "Ocp-Apim-Subscription-Key" : FACES_KEY
            }

            if response["output"]["text"] == "$foto_identidade":
                r = requests.post(detectUrl, data=decoded, headers=headers)
                data = r.json()
                if len(data['faceId']) != 2:
                    sucesso = "Não" 
                else:
                    headers = {
                        "Content-Type" : "application/json",
                        "Ocp-Apim-Subscription-Key" : FACES_KEY
                    }
                    body = {
                        "faceId1" : data['faceId'][0],
                        "faceId2" : data['faceId'][1],
                    }

                    r = requests.post(verifyUrl, data=body, headers=headers)
                    data = r.json()
                    confidence = data['confidence']

                    if confidence < 0.4:
                        sucesso = "Não"   

            elif response["output"]["text"] == "$foto_contrato":
                x = "x"
            elif response["output"]["text"] == "$foto_poste":
                x = "x"
            else:
                sucesso = uuid.uuid4().hex

            response = assistant.message(
                workspace_id=workspace_id,
                input={
                    'text': sucesso
                },
                context= req["context"]
            ).get_result()

        return jsonify(resposta=response["output"]["text"],context=response["context"]) 

#Endpoint GET para identificar usuario
@app.route('/criardado')
def createData():
    clientes = [{
        "_id" : "1",
        "nome" : "Thais",
        "sobrenome" : "Araujo",
        "idade" : "25",
        "perfil" : "noob",
        "data_criacao" : datetime.now().isoformat(),
        "avatar": "https://www.stickees.com/files/avatars/male-avatars/1697-andrew-sticker.png"
    },{
        "_id" : "2",
        "nome" : "Roberto",
        "sobrenome" : "Carlos",
        "idade" : "55",
        "perfil" : "conservador",
        "data_criacao" : datetime.now().isoformat(),
        "avatar": "https://image.flaticon.com/icons/svg/145/145850.svg"
    },{
        "_id" : "3",
        "nome" : "Carmen",
        "sobrenome" : "Sandiego",
        "idade" : "39",
        "perfil" : "semtempo",
        "data_criacao" : datetime.now().isoformat(),
        "avatar": "https://image.flaticon.com/icons/svg/145/145850.svg"
    }]

    for cliente in clientes:
        clienteCol = db.cliente
        clienteCol.insert_one(cliente)
        clienteEs = prepareMongoToEs(cliente)
        es.index(index="cliente", doc_type='doc_cliente', id=uuid.uuid4().hex, body=clienteEs)

    return "The mock is a lie"

def prepareMongoToEs(data):
    data["mongo_id"] = data["_id"]
    del data["_id"]
    return data


if __name__ == '__main__':
    app.run(debug=True)