from page import page
from kindservicetable import kindServiceTable
from kindserviceeditform import kindServiceEditForm

class kindServicePage(page):
    def __init__(self,cleaner,parent=None):
        page.__init__(self,cleaner=cleaner,parent=parent)
        self.setTable(kindServiceTable(cleaner=cleaner,parent=parent))
        self.setForm(kindServiceEditForm(cleaner=cleaner,parent=parent))
        self.setConnect()
