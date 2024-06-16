#-*- coding:utf-8 -*-
from client import client

class ClientList:
    def __init__(self):
        self.__list=[]
    def clear(self):
        self.__list=[]
    def findByCode(self,code):
        for l in self.__list:
            if l.getCode()==code:
                return l
    def getNewCode(self):
        return max(self.getCodes())+1
    def getCodes(self):
        return [s.getCode() for s in self.__list]
    def getItems(self):
        return self.__list
    def appendItem(self, value):
        if isinstance(value, client):
            self.__list.append(value)
    def removeItem(self, value):
        if isinstance(value, client):
            self.__list.remove(value)
        if isinstance(value, int):
            client = self.findByCode(value)
            if client:
                self.__list.remove(client)
    def createItem(self, code=0, surname="", name="", secname="", regular=0):
        if code in self.getCodes():
            print('Client with code %s already exists' % code)
        else:self.appendItem(client(code, surname, name, secname, regular))
    def newItem(self, surname="", name="", secname="", regular=0):
            c = client(self.getNewCode(), surname, name, secname, regular)
            self.appendItem(c)
            return c