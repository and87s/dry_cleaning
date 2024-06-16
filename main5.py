import sys,os
import datetime
import cherrypy
from cherrypy import tools
from drycleaning import dryСleaning
from dataxml import dataxml
from servicetablewebpage import serviceTableWebPage
from serviceeditwebpage import serviceEditWebPage

class root:
    def __init__(self):
        self.__cleaner=dryСleaning()
        self.__dataxml=dataxml(self.__cleaner)
        self.__dataxml.readFile('oldfile.xml')
        self.wt = serviceTableWebPage(self.__cleaner)
        self.ef = serviceEditWebPage(self.__cleaner)
    
    def index(self):
        return self.wt.index()
    
    def editform(self, **kwargs):
        if cherrypy.request.method == 'POST':
            c = self.__cleaner.getService(int(kwargs['code']))
            c.setClient(self.__cleaner.getClient(int(kwargs['client'])))
            c.setKindService(self.__cleaner.getKindService(int(kwargs['kindService'])))
            c.setCount(int(kwargs['count']))
            raise cherrypy.HTTPRedirect('/')
        else:
            self.ef.setCode(kwargs['code'])
            return self.ef.index()
    
    def delr(self, code=''):
        self.__cleaner.removeService(int(code))
        raise cherrypy.HTTPRedirect('/')
    def add(self):
        s = self.__cleaner.newService()
        raise cherrypy.HTTPRedirect('/editform?code=%s' % s.getCode())
    
    def receptionItem(self, code = 0):
        if int(code):
            service = self.__cleaner.getService(int(code))
            if service:
                service.setDateReception(datetime.now())
        raise cherrypy.HTTPRedirect('/')

    def returnItem(self, code = 0):
        if int(code):
            service = self.__cleaner.getService(int(code))
            if service:
                service.setDateReturn(datetime.now())
        raise cherrypy.HTTPRedirect('/')

    index.exposed=True
    editform.exposed=True
    delr.exposed=True
    add.exposed=True
    receptionItem.exposed=True
    returnItem.exposed=True

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