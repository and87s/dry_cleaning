#-*- coding:utf-8 -*-
from general import general

class generalList:
    def __init__(self):self.__list=[]
    def clear(self):self.__list=[]
    def findByCode(self,code):
        for l in self.__list:
            if l.getCode()==code: return l
    def getNewCode(self):
        if len(self.__list) == 0:
            return 1
        return max(self.getCodes()) + 1
    def getCodes(self):return [s.getCode() for s in self.__list]
    def getItems(self) -> list[general]:
        return self.__list
    def appendItem(self, value):
        if isinstance(value, general):
              self.__list.append(value)
    def removeItem(self, value):
        if isinstance(value, general):
            self.__list.remove(value)
        if isinstance(value, int):
            self.__list.remove(self.findByCode(value))
    def getList(self): return self.__list