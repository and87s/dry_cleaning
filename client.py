#-*- coding:utf-8 -*-
from general import general

class client:
    def __init__(self,code=0,surname='',name='',secname='',regular = False ):
        self.setSurname(surname)
        self.setCode(code)
        self.setName(name)
        self.setSecname(secname)
        self.setRegular(regular)
    def setSurname(self,value):
        self.__surname=value
    def setName(self,value):
        self.__name=value
    def setSecname(self,value):
        self.__secname=value
    def setRegular(self,value):
        self.__regular= bool(value)
    def setCode(self,value):
        self.__code=value
    def getSurname(self):
        return self.__surname
    def getName(self):
        return self.__name
    def getSecname(self):
        return self.__secname
    def getRegular(self):
        return self.__regular
    def getCode(self):
        return self.__code
    def getDecription(self):
        return '%s %s %s' %(self.__surname, self.__name, self.__secname)