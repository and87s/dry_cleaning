import sys,os
import cherrypy
from drycleaning import dryСleaning
from dataxml import dataxml
from servicetablewebpage import serviceTableWebPage

class root:
    def __init__(self):
        self.__cleaner=dryСleaning()
        self.__dataxml=dataxml(self.__cleaner)
        self.__dataxml.readFile('oldfile.xml')
        self.wt=serviceTableWebPage(self.__cleaner)
    def index(self):
        return self.wt.index()
    index.exposed=True

if __name__ == '__main__':
    conf = {
    '/': {
        'tools.sessions.on': True,
        'tools.staticdir.root': os.path.abspath(os.getcwd())
    },
    '/static': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': './public'
    }
}

cherrypy.quickstart(root(), '/', conf)