import uuid
import base64
import requests
import json
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

bot = ChatBot('CPFL ChatBot',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.70,
            'response_selection_method': get_first_response
        }
    ]
)

conversas = []

conversas.append(['Oi',
    'Posso te ajudar com alguma coisa ?',
    'Eu estou de mudança e preciso trocar o titular',
    'Claro. Você sabe como fazer isso ?',
    'Não',
    'Alguem mora no endereço atualmente ? Preciso saber se lá já possui luz',
    'Sim, moram lá.',
    'Entendi, então faremos uma transferencia de titular. Para qual endereço você vai se mudar ?',
    '$$endereço$$',
    'Obrigado, agora preciso só que me confirme sua identidade. Pode me mandar uma foto sua segurando seu RG (com a foto pra camera)?',
    '$$foto_usuario$$',
    'Ficou ótimo, conseguimos te ver bem. Última coisa, você poderia mandar uma foto do contrato da casa, de aluguel ou algo do tipo ?',
    '$$foto_contrato$$',
    'Perfeito, já tenho todas as informações que preciso! Em breve ligaremos confirmando a sua troca de titularidade.'
])

conversas.append(['Olá',
    'Posso te ajudar com alguma coisa ?',
    'Quero realizar a troca de titular',
    'Claro. Você sabe como fazer isso ?',
    'Sim',
    'Entendi, então faremos uma transferencia de titular. Para qual endereço você vai se mudar ?',
    '$$endereço$$',
    'Obrigado, agora preciso só que me confirme sua identidade. Pode me mandar uma foto sua segurando seu RG (com a foto pra camera)?',
    '$$foto_usuario$$',
    'Ficou ótimo, conseguimos te ver bem. Última coisa, você poderia mandar uma foto do contrato da casa, de aluguel ou algo do tipo ?',
    '$$foto_contrato$$',
    'Perfeito, já tenho todas as informações que preciso! Em breve ligaremos confirmando a sua troca de titularidade.'
])

conversas.append(['Olá',
    'Posso te ajudar com alguma coisa ?',
    'Quero fazer uma transferencia de titular',
    'Claro. Você sabe como fazer isso ?',
    'Sim',
    'Entendi, então faremos uma transferencia de titular. Para qual endereço você vai se mudar ?',
    '$$endereço$$',
    'Obrigado, agora preciso só que me confirme sua identidade. Pode me mandar uma foto sua segurando seu RG (com a foto pra camera)?',
    '$$foto_usuario$$',
    'Ficou ótimo, conseguimos te ver bem. Última coisa, você poderia mandar uma foto do contrato da casa, de aluguel ou algo do tipo ?',
    '$$foto_contrato$$',
    'Perfeito, já tenho todas as informações que preciso! Em breve ligaremos confirmando a sua troca de titularidade.'
])

conversas.append(['Bom dia',
    'Bom dia, posso te ajudar com alguma coisa ?',
    'Vou fazer uma mudança.',
    'Claro. Você sabe como fazer isso ?',
    'Ainda não',
    'Alguem mora no endereço atualmente ? Preciso saber se lá já possui luz',
    'Não a casa é nova',
    'Entendi, então faremos a instalação de um novo ponto. Para qual endereço você vai se mudar ?',
    '$$endereço$$',
    'Obrigado, agora preciso só que me confirme sua identidade. Pode me mandar uma foto sua segurando seu RG (com a foto pra camera)?',
    '$$foto_usuario$$',
    'Ficou ótimo, conseguimos te ver bem. você poderia mandar uma foto do contrato da casa, de aluguel ou algo do tipo ?',
    '$$foto_contrato$$',
    'Perfeito, só precisamos de mais uma informação. O pote próximo precisa estar de acordo com nosso regulamento como descrito nesse link, ele está de acordo?',
    'Sim está',
    'Você poderia nos mandar uma foto dele ?',
    '$$foto_poste$$',
    'Já tenho todas as informações que preciso! Em breve ligaremos confirmando a sua instalação.'
])

trainer = ListTrainer(bot)
for conversa in conversas:    
    trainer.train(conversa)

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

        return jsonify(cliente=cliente,sessao=sessao) 
        
    if request.method == 'POST':
        req = request.json
        resp = bot.get_response(req['resposta'])

        if req['foto'] != None and req['foto'] != "":
            decoded = base64.decodebytes(req['foto'])

            

            headers = {
                "Content-Type" : "application/octet-stream",
                "Ocp-Apim-Subscription-Key" : FACES_KEY
            }

            r = requests.post(detectUrl, data=decoded, headers=headers)
            data = r.json()

            if len(data['faceId']) != 2:
                return 



            headers = {
                "Content-Type" : "application/json",
                "Ocp-Apim-Subscription-Key" : FACES_KEY
            }

            body = {
                "faceId1" : data['faceId'][0],
                "faceId1" : data['faceId'][1],
            }

            r = requests.post(verifyUrl, data=body, headers=headers)
            data = r.json()

            confidence = data['confidence']

            resp = {"text":"sucesso"}
            
        mensagem = {
            
        }
        mensagemCol = db.messagem


        return jsonify(menssagem={"sucesso":"true","resposta":resp.text}) 

#Endpoint GET para identificar usuario
@app.route('/criardado')
def createData():
    clientes = [{
        "_id" : "1",
        "nome" : "Thais",
        "sobrenome" : "Araujo",
        "idade" : "25",
        "perfil" : "noob",
        "data_criacao" : datetime.now().isoformat()
    },{
        "_id" : "2",
        "nome" : "Roberto",
        "sobrenome" : "Carlos",
        "idade" : "55",
        "perfil" : "conservador",
        "data_criacao" : datetime.now().isoformat()
    },{
        "_id" : "3",
        "nome" : "Carmen",
        "sobrenome" : "Sandiego",
        "idade" : "39",
        "perfil" : "semtempo",
        "data_criacao" : datetime.now().isoformat()
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