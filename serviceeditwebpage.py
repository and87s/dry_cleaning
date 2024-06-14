from webpage import webPage
from servicewebform import serviceWebForm

class serviceEditWebPage(webPage):
    def __init__(self,cleaner=None):
        webPage.__init__(self)
        self.__form=serviceWebForm(cleaner=cleaner)
            
    def setCode(self, code:int):
        self.__form.setCode(code)
        
    def middle(self):
        s=self.__form.update()
        return s