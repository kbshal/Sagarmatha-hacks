from flask import Flask, request, jsonify
from flask import request
import os
import requests
from dotenv import load_dotenv
from os.path import join, dirname


dotenv_path = join(dirname(__file__), 'creds/.env')
load_dotenv(dotenv_path)


app=Flask(__name__)

application = app

auth_key=os.getenv("AUTH_KEY")
model_name=os.getenv("MODEL_NAME")
context=os.getenv("PROMPT")
url=os.getenv("URL")

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + (auth_key)
}

@app.get("/")
def hello():
    return "Hello Moye Moye"



@app.route("/api/prompt/", methods=["POST"])
def get_prompt():
    
    #print(request.json)
    data=(request.json)["prompt"]
    print(data)
    
    json_data = {
    'model': str(model_name),
    'messages': [
        {
            'role': 'system',
            'content': str(context),
        },
        {
            'role': 'user',
            'content': f'{data}',
        },
    ],
}
    response = requests.post(url, headers=headers, json=json_data)
    
    response=response.json()
    response=response["choices"][0]["message"]["content"]
    return response



