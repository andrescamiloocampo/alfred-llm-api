from flask import Flask,request
from utils import dsConnection

app = Flask(__name__)

@app.route("/chat",methods=['POST'])
def hello_world():    
    request_data = request.get_json()
    print(request_data)
    try:        
        response = dsConnection.client.chat.completions.create(
        model='deepseek/deepseek-r1:free',
        messages=[         
            {"role":"system","content":"Eres un profesor experto de ingles y solo respondes en ese idioma"},        
            request_data
        ],
        stream=False
        )
        return response.choices[0].message.content
    except Exception as e:
        return f'Error connecting to the api: {e}'    