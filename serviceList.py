#-*- coding:utf-8 -*-
from datetime import datetime
from generalList import generalList
from service import service

class ServiceList(generalList):
    def appendItem(self, value):
          if isinstance(value, service):
              generalList.appendItem(self, value)
    def createItem(self, code=0, kindService=None, count=0, client=None, dateReception=None, dateReturn=None):
        if code in self.getCodes():
            print('Service with code %s already exists' % code)
        else:self.appendItem(service(code, kindService, count, client, dateReception, dateReturn))

    def removeItem(self, value):
        #self.__list.remove(value)
        if isinstance(value, int):
            s = self.findByCode(value)
            if s:
                generalList.removeItem(self, s)
        if isinstance(value, service):
            generalList.removeItem(self, value)
    
    def newItem(self, kindService, count, client, dateReception, dateReturn):
            b = service(self.getNewCode(), kindService, count, client, dateReception, dateReturn)
            self.appendItem(b)
            return b
    
    def getCountClient(self, value):
        i = 0
        for l in self.getList():
            if l.getClient() == value: i = i+1
        return i
    def receptionItem(self,value):
        if isinstance(value, service): self.appendItem(value)
        value.setDateReception(datetime.now())
        client = value.getClient()
        if client.getRegular != True:
            if self.getCountClient(client) >= 3:
                client.setRegular(True)
    def returnItem(self, value):
        if isinstance(value, service): value.setDateReturn(datetime.now())