import os

from flask import Flask
from flask import request

import requests

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from upstream import Upstream

app = Flask(__name__)
upstream = None

@app.route('/')
def home():
    return "The homepage."

@app.route('/connect')
def connect():
    global upstream
    upstream = Upstream(get_database_info('ip'), '/halt')
    if not upstream:
        return 'Error setting upstream.'
    return 'Upstream has been set succesfully.'

@app.route('/move/<string:subpath>')
def move(subpath):
    global upstream
    if not upstream:
        return 'Upstream not set.'
    upstream.set_path(subpath)
    response = requests.get(upstream.get_base_url() + upstream.get_path())
    return response.text

def get_database_info(key):
    ref = db.reference(key)
    value = ref.get()
    return value

def main():
    certificatePath = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    print("Certificate Path: " + certificatePath)
    cred = credentials.Certificate(certificatePath)
    firebase_app = firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://sf-cads.firebaseio.com'
    })

main()