#-*- coding:utf-8 -*-
from kindservice import kindService

class KindServiceList:
    def __init__(self):self.__list=[]
    def clear(self):self.__list=[]
    def findByCode(self,code):
        for l in self.__list:
            if l.getCode()==code:
                return l
    def getNewCode(self):return max(self.getCodes())+1
    def getCodes(self):return [s.getCode() for s in self.__list]
    def getItems(self):return [s for s in self.__list]
    def removeItem(self,value):
        if isinstance(value,kindService):self.__list.remove(value)
        if isinstance(value,int):self.__list.remove(self.findByCode(value))
    def appendItem(self,value):
        if isinstance(value,kindService):self.__list.append(value)
    def createItem(self,code=0,name = '', typeservice = '', price = 0):
        if code in self.getCodes():print('KindService with code %s already exists')
        else:self.appendItem(kindService(code,name,typeservice,price))
    def newItem(self,name,typeservice,price):
        self.appendItem(kindService(self.getNewCode(),name,typeservice,price))