from cleanerwidget import cleanerWidget

class webTable(cleanerWidget):

    def __init__(self,cleaner=None,header=[]):
        cleanerWidget.__init__(self,cleaner)
        self.setHeader(header)
        #self.setHeaderBgColor(headerBgColor)

    def setHeader(self,value=[]):
        self.__header=value

    def getHeader(self,value=[]):
        return self.__header

    def __start(self):
        self.__numLines=0
        s='<table class="table table-striped"><thead><tr><th class=header></th>'
        for k in self.getHeader():
            s+='<th class=header>%s</th>'%k
        s+='</tr></thead><tbody>'
        return s
        
    def appendLine(self,code=0,value=[]):
        self.__numLines+=1
        bg=''
        if ((self.__numLines % 2) == 0):bg=' class=evenline'
        if ((self.__numLines % 2) != 0):bg=' class=oddline'
        s='<tr%s><td>%s</td>'%(bg,self.__numLines)
        for k in value:
            s+='<td>%s</td>'%k
        s+='<td><a type="button" class="btn btn-secondary" href=editform?code=%s>редактировать</a></td><td><a type="button" class="btn btn-danger" href=delr?code=%s>удалить</a></td></tr>'%(code,code)
        return s
    
    def __end(self):
        return """
        </tbody></table>
        <div class="col">
        </div>
        <div class="col-md-2">
            <a class="btn btn-primary" href="add" role="button">Добавить</a>
        </div>"""
        
    def setData(self):
        return ''
    
    def update(self):
        return self.__start()+self.setData()+self.__end()