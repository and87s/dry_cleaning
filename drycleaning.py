#-*- coding:utf-8 -*-
from clientlist import ClientList
from serviceList import ServiceList
from kindservicelist import KindServiceList
from general import general
from service import service
from client import client
from kindservice import kindService

class dryСleaning():
   def __init__(self):
      self.__clientlist=ClientList()
      self.__serviceList=ServiceList()
      self.__kindServiceList=KindServiceList()
   def clear(self):
      self.__clientlist.clear()
      self.__serviceList.clear()
      self.__kindServiceList.clear()
   def createClient(self,code=0,surname='',name='',secname='', regular =0):
      self.__clientlist.createItem(code,surname,name,secname,regular)
   def newClient(self,surname='',name='',secname='',regular =0):
      self.__clientlist.newItem(surname,name,secname,regular)
   def removeClient(self,value):
      self.__clientlist.removeItem(value)
   def getClient(self,code):return self.__clientlist.findByCode(code)
   def getClientList(self) -> list[client] :return self.__clientlist.getItems()
   def getClientCodes(self):return self.__clientlist.getCodes()
   def createService(self,code=0,kindService = None, count = 0, client = None,dateReception = None,dateReturn = None):
      self.__serviceList.createItem(code,kindService,count,client,dateReception,dateReturn)
   def newService(self,code, kindService = None, count = 0, client = None,dateReception = None,dateReturn = None):
      self.__serviceList.newItem(code,kindService,count,client,dateReception,dateReturn)
   def removeService(self,code,kindService = None, count = 0, client = None, dateReception = None, dateReturn = None):
      self.__serviceList.removeItem(code)
      for b in self.__serviceList.getItems():
         b.setService(None)
   def getService(self,code):return self.__serviceList.findByCode(code)
   def getServiceList(self) -> list[service]:
      return self.__serviceList.getItems()
   def getServiceCodes(self) -> list[int]:
      return self.__serviceList.getCodes()
   def createKindService(self,code=0,name = '', typeservice = '', price = 0):
      self.__kindServiceList.createItem(code,name, typeservice,price)
   def newKindService(self,code=0,name = '', typeservice = '', price = 0):
      self.__kindServiceList.newItem(code,name, typeservice,price)
   def removeKindService(self,code):self.__kindServiceList.removeItem(code)
   def getKindService(self,code):
      return self.__kindServiceList.findByCode(code)
   def getKindServiceList(self)  -> list[kindService]:
      return self.__kindServiceList.getItems()
   def getKindServiceCodes(self) -> list[int]:
      return self.__kindServiceList.getCodes()