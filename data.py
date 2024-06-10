#-*- coding:utf-8 -*-

class data:
    def __init__(self,ras=None,inp='',out=''):
        self.setRas(ras)
        self.setInp(inp)
        self.setOut(out)
    def setRas(self,value):self.__ras=value
    def setInp(self,value):self.__inp=value
    def setOut(self,value):self.__out=value
    def getRas(self):return self.__ras
    def getInp(self):return self.__inp
    def getOut(self):return self.__out
    def readFile(self,filename):
        self.setInp(filename)
        self.read()
    def writeFile(self,filename):
        self.setOut(filename)
        self.write()
    def read(self):pass
    def write(self):pass   