import sys,os
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
    
    @cherrypy.expose
    @tools.decode(encoding='ISO-88510-1')
    def editform(self, cancel = False, **kwargs):
        if cherrypy.request.method == 'POST':
            if cancel:
                raise cherrypy.HTTPRedirect('/')
            cherrypy.HTTPRedirect('/')

            
        self.ef.setCode(**kwargs['code'])
        return self.ef.index()
    
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