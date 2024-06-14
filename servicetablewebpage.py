from webpage import webPage
from servicewebtable import serviceWebTable

class serviceTableWebPage(webPage):
    def __init__(self,cleaner=None):
        webPage.__init__(self)
        self.__table=serviceWebTable(cleaner=cleaner)
    
    def middle(self):
        s=self.__table.update()
        return """
        <div class="row py-md-5">%s</div>""" % (s)