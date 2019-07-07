import configWorkspace
import sys
import uuid
import base64
import binascii
import codecs
import requests
import json
import urllib.parse
import random
from pymongo import MongoClient
from flask import Flask, request, jsonify  
from flask_cors import CORS
from datetime import datetime
from elasticsearch import Elasticsearch
from ibm_watson import AssistantV1
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import FaceAttributeType, TrainingStatusType, Person


app = Flask(__name__)
CORS(app)

API_FACES_ENDPOINT = 'https://radixhack.cognitiveservices.azure.com/face/v1.0/'
detectUrl = API_FACES_ENDPOINT+"detect"
verifyUrl = API_FACES_ENDPOINT+"verify"
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

face_client = FaceClient(API_FACES_ENDPOINT, CognitiveServicesCredentials(FACES_KEY))

workspace = assistant.get_workspace(workspace_id="0f156808-de0f-4c7c-a97f-408808cabe79").get_result()
workspace_id = workspace['workspace_id']

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
        
        resposta = []
        for resp in response["output"]["text"]:
            resposta.append(resp.replace("#nome", cliente["nome"]))

        return jsonify(cliente=cliente, resposta=resposta, context=response["context"]) 
        
    if request.method == 'POST':
        req = request.json       
        response = assistant.message(
            workspace_id=workspace_id,
            input={
            'text': req["text"]
            },
            context= req["context"]
        ).get_result()

        mensagem = {
            "_id" : uuid.uuid4().hex,
            "texto": req["text"],
            "data_insercao" : datetime.now().isoformat()
        }

        mensagemCol = db.mensagem
        mensagemCol.insert_one(mensagem)
        mensagem = prepareMongoToEs(mensagem)
        es.index(index="mensagem", doc_type='doc_mensagem', id=uuid.uuid4().hex, body=mensagem)

        if req['foto'] != None and req['foto'] != "":
            sucesso = "Sim" 
            if response["output"]["text"][0] == "foto_identidade":
                #Tentativa 1
                #decoded = binascii.a2b_base64(req['foto'])
                #headers = {
                #    "Content-Type" : "application/octet-stream",
                #    "Ocp-Apim-Subscription-Key" : FACES_KEY
                #}
                #r = requests.post(detectUrl, decoded, headers=headers)
                #Tentativa 2
                #filename = "imageToSave"  + datetime.now().isoformat() + ".jpg"
                #with open(filename, "wb") as fh:
                #    fh.write(base64.binascii.a2b_base64((req['foto'])))
                #with open(filename, "rb") as fh:
                #r = face_client.face.detect_with_stream(fh)

                #Mock due to service instability to send file
                data = [{
                        "faceId": "0d082829-79fb-4e76-8360-d2cc78b84e9c",
                        "faceRectangle": {
                            "top": 733,
                            "left": 543,
                            "width": 809,
                            "height": 809
                        }
                    },
                    {
                        "faceId": "bdfd3de7-70eb-4f55-bf8c-d7d4391d1134",
                        "faceRectangle": {
                            "top": 1410,
                            "left": 166,
                            "width": 155,
                            "height": 155
                        }
                    }
                ]
              
                if len(data) < 2:
                    sucesso = "Não" 
                else:
                    headers = {
                        "Content-Type" : "application/json",
                        "Ocp-Apim-Subscription-Key" : FACES_KEY
                    }
                    body = {
                        "faceId1" : data[0]['faceId'],
                        "faceId2" : data[1]['faceId'],
                    }

                    #r = requests.post(verifyUrl, data=body, headers=headers)
                    #data = r.json()

                    data = {
                        "confidence" : 0.8
                    }
                    confidence = data['confidence']

                    if confidence < 0.4:
                        sucesso = "Não"   

            elif response["output"]["text"][0] == "#foto_contrato":
                x = "x"
            elif response["output"]["text"][0] == "#foto_poste":
                x = "x"
            else:
                sucesso = uuid.uuid4().hex

            response = assistant.message(
                workspace_id=workspace_id,
                input={
                    'text': sucesso
                },
                context=response["context"]
            ).get_result()

        return jsonify(resposta=response["output"]["text"],context=response["context"]) 
            


def prepareMongoToEs(data):
    data["mongo_id"] = data["_id"]
    del data["_id"]
    return data


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

#Endpoint GET para identificar usuario
@app.route('/criarmuitodado')
def createDataBulk():
    perfis = ["noob","semtempo","conservador"]
    clientes = []
    for i in range(100):
        clientes.append({
            "_id" : uuid.uuid4().hex,
            "nome" : "Cliente_" + str(i),
            "idade" : random.randint(25,60),
            "perfil" : perfis[random.randint(0,5)%3],
            "data_criacao" : datetime.now().isoformat(),
            "avatar": "https://www.stickees.com/files/avatars/male-avatars/1697-andrew-sticker.png"
        })

    for cliente in clientes:
        clienteCol = db.cliente
        clienteCol.insert_one(cliente)
        clienteEs = prepareMongoToEs(cliente)
        es.index(index="cliente", doc_type='doc_cliente', id=uuid.uuid4().hex, body=clienteEs)

    return "Fim"

if __name__ == '__main__':
    app.run(debug=True)