from flask import Flask
from flask import request, render_template, redirect, url_for, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
#from config import BaseConfig
from os import environ



app = Flask(__name__)



@app.route('/test', methods=['GET'])
def test():
  return make_response(jsonify({'message': 'test route'}), 200)



@app.route('/', methods=['GET'])
def index():
    return 'Im slave'
