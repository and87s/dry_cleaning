#-*- coding:utf-8 -*-
from general import general

class kindService: 
    def __init__(self, code, name = '', typeservice = '', price = 0):
        self.setCode(code)
        self.setName(name)
        self.setTypeService(typeservice)
        self.setPrice(price)
    def setCode(self, value):
        self.__code = value
    def setName(self, value):
        self.__name = value
    def setTypeService(self, value):
        self.__typeofservice = value
    def setPrice(self, value):
        self.__price = int(value)
    def getName(self):
        return self.__name
    def getTypeService(self):
        return self.__typeofservice
    def getPrice(self):
        return self.__price
    def getCode(self):
        return self.__code