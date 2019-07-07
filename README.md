##Descrição
Aplicação backend da hackaton radix 2019 
Link do repositorio do front end https://github.com/rafaelbatistamarcilio/hackathon-radix-2019
 
Aplicação que realiza a tratação de dados para comunicação entre front end e inteligencia criada Watson
Alem de buscar e amarzenar os dados, e salva-los em um banco Elastic Search para futura configuração de um DashBoard Kibana 

##Como executar o projeto

Você precisará do Python3 e pip3

Entrar no ambiente virtual (pelo linux pode-se fazer através do comando source env/bin/activate) dentro da pasta raiz do projeto.

Baixar as dependências do Python através do comando pip3 install -r requirements.txt

Executar o comando python app.py

Acessar através do link http://127.0.0.1:5000/

Utilizar alguma ferramenta (como postman) para enviar requisições.

##Endpoints
Inicio se da pelo chat 
GET http://127.0.0.1:5000/chat?id=<ID DO CLIENTE>

Exemplos para teste
<ID DO CLIENTE>( 1,2 ou 3)[1:Perfil noob, 2:Perfil conservador, 3: Perfil semtempo]

POST http://127.0.0.1:5000/chat
{
    "text": "Mensagem do chat",
    "foto": "",
    "context" *Utilizar o context retornado na última requisição, incluindo GET
}


##Conteudo 
Arquivo configWorkspace.py contem configuração do IBM Watson