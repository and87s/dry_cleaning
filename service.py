#-*- coding:utf-8 -*-
import datetime
from general import general
from kindservice import kindService
from client import client

class service(general):
    def __init__(self,code=0,kindService = None, count = 0, client = None,dateReception: datetime = None,dateReturn:datetime = None):
        general.__init__(self,code)
        self.setCode(code)
        self.setClient(client)
        self.setKindService(kindService)
        self.setCount(count)
        self.setDateReception(dateReception)
        self.setDateReturn(dateReturn)
    def setKindService(self, value):
        if isinstance(value, kindService): 
            self.__kindService = value 
    def setClient(self, value):
        if isinstance(value, client): 
            self.__client = value
    def setDateReception(self, value):
            self.__dateReception = value
    def setDateReturn(self, value):
            self.__dateReturn = value
    def setCount(self,value):
            self.__count = value
    def setSum(self,value): 
            self.__sum = value
    def getKindService(self):
            return self.__kindService
    def getClient(self) -> client:
            return self.__client
    def getDateReception(self) -> datetime:
            return self.__dateReception
    def getDateReturn(self) -> datetime:
            return self.__dateReturn
    def getPrice(self):
            return self.__kindService.getPrice() 
    def getCount(self):
            return self.__count
    def getSum(self):
            return self.__sum
    def finalprice(self) -> float:
        result = 0.0
        s=self.getClient().getRegular()
        q=self.getKindService().getPrice()
        count=self.getCount()
        if s==1:
            count=0.97*count
        q=q*count
        d1=self.getDateReception()
        d2=self.getDateReturn()
        result=((d2-d1).days+1)*q
        return result
    def calculate(self):
        discount = 0
        s=self.getClient().getRegular()
        q=self.getKindService().getPrice()
        if self.__client.getRegular() == True: discount = 0.03
        self.__sum = self.__count * self.__kindService.getPrice()*(1-discount);        
    def print(self):
        print('Client - ', self.getClient().getSurname(),' ',self.getClient().getName(),' ',self.getClient().getSecname(),'; ','KindService - ',self.getKindService().getTypeService(), 
        '; ', 'finalprice - ',self.finalprice())
    def getDecription(self):
        s = ''
        s = '%s %s %s %s %s' %(self.getClient().getDecription(), self.getKindService().getName(), self.getPrice(), self.getCount(), self.finalprice())
        return s