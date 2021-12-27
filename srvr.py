import socket
import sys
import threading
from db import dbtools
import pickle
from obj import *

def main(port):
    sck=socket.socket()
    ip="127.0.0.1"
    yes='yes'
    no='no'
    sck.bind((ip, port))
    print("binding successful i guess\nwaiting for connection... ugh")

    connection=dbtools.connect("localhost", "root", "", "users")
    dbtools.execute(connection,"CREATE DATABASE users")

    clients=[]

    def uyy():
        sck.listen(1) 
        conn,add=sck.accept()

        client=pickle.loads(msg).get_username()

        frname=pickle.loads(msg).get_friend_name()
        
        password=pickle.loads(msg).get_password()

        passs="SELECT password FROM `users` WHERE username='"+client+"';"
        res = dbtools.read(connection, passs)
        if("[('"+password+"',)]" == str(res)):
            print(client+" has logged in")
            conn.send(yes.encode())
        else:
            conn.send(no.encode())

        clients.append(client)
        

        def hej():
            while True:
                msg=pickle.loads(msg).get_message()
                if msg=='':
                    continue
                if msg=='!end':
                    clients.remove(client)
                    continue

                requests.put(f"http://127.0.0.1:5000/api/{client}/{frname}/{password}/{msg}")

        def monika():
            x=0
            k=0
            while True:
                file=open("api/"+frname+client,'r+')
                lines=file.readlines()
                if(x!=lines):
                    i=0
                    for line in lines:
                        i+=1
                        if k<i:
                            try:
                                conn.send(pickle.dumps(username=client,password=password,friend_username=frname("{}: {}\n".format(frname,line.strip())).encode()))
                            except:
                                pass
                            k+=1
                file.close()
                x=lines

        t1=threading.Thread(target=hej,args=())
        t2=threading.Thread(target=monika,args=())
        t1.start()
        t2.start()

    a=[]
    for i in range(10000):
        a.append(0)
    k=0
    while True:
        a[k]=threading.Thread(target=uyy,args=())
        a[k].start()
        a[k].join()
        k+=1