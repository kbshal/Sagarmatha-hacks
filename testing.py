from flask import Flask, request, jsonify
from flask import request
import os
import requests
from dotenv import load_dotenv
from os.path import dirname, join

dotenv_path = join(dirname(__file__), 'creds/.env')
print(dotenv_path)
load_dotenv(dotenv_path)

auth_key=os.getenv("AUTH_KEY")
model_name=os.getenv("MODEL_NAME")
prompt=os.getenv("PROMPT")
print(auth_key, model_name)
print(prompt)