class formElement():
    def __init__(self, id=None, name = None, cl=None) -> None:
        self.setId(id)
        self.setName(name)
        self.setClass(cl)
    
    def setId(self,value=''):
        self.__id=value

    def getId(self):
        return self.__id
    
    def setName(self,value=''):
        self.__name=value

    def getName(self):
        return self.__name
    
    def setClass(self,value=''):
        self.__class=value

    def getClass(self):
        return self.__class
    
    def update(self):
        pass