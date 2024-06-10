import sys,os
import cherrypy
from drycleaning import dryСleaning
from dataxml import dataxml

class root:
    def __init__(self):
        self.__lib=library()
        self.__dataxml=dataxml(self.__lib)
        self.__dataxml.readFile('old.xml')
        self.wt=booksTableWebPage(self.__lib)
    def index(self):
        return self.wt.index()
    index.exposed=True