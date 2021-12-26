import socket
import sys
import threading
import os
import hashlib
import srvr

class Absmsg(metaclass=srvr.ABCMeta):
    @srvr.abstractclassmethod
    def get_message():
        pass
    def get_username():
        pass
    def get_password():
        pass
    def get_friend_name():
        pass


class Message(Absmsg):
    def __init__(self,username,password,friend_name,message):
        self.username=username
        self.message=message
        self.password=password
        self.friend_name=friend_name

    def get_username(self):
        return self.username

    def get_message(self):
        return self.message

    def get_password(self):
        return self.password

    def get_friend_name(self):
        return self.friend_name
