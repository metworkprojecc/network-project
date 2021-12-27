from flask import *
import json
from flask_restful import Resource, reqparse, Api
import mysql.connector
from mysql.connector import Error
import pandas as pd
import hashlib
import socket
import sys
import threading
import os
import srvr
from db import dbtools

temp=threading.Thread(target=srvr.main, args=(4444,))
temp.start()

app = Flask(__name__)

api = Api(app=app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    repassword = request.form['repassword']
    if password != repassword:
        return redirect(url_for('register'))
    password = hashlib.sha256(password.encode("utf-8")).hexdigest()
    connection=dbtools.connect("localhost", "root", "", "users")
    dbtools.execute(connection,"INSERT INTO users (username,password) VALUES ('" + username + "','" + password + "');")
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    if(request.method=='POST'):
        sck.send(name.encode())
        tname=(sck.recv(4096)).decode()
        sck.send(frname.encode())
        tname=(sck.recv(4096)).decode()
        password=hashlib.sha256(password.encode("utf-8")).hexdigest()
        sck.send(password.encode())
        tname=(sck.recv(4096)).decode()
        if tname=='yes':
            return redirect(url_for('chat',sckk=sck))
        else:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
        
#sck contains request from server (username, friend's username, password and message)
@app.route('/chat/<sckk>',methods=['GET','POST'])
def chat(sckk):
    srvr(4444)
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)