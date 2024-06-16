from page import page
from clientable import clientTable
from clienteditform import clientEditForm

class clientPage(page):
    def __init__(self,cleaner,parent=None):
        page.__init__(self,cleaner=cleaner,parent=parent)

        self.setTable(clientTable(cleaner=cleaner,parent=parent))
        self.setForm(clientEditForm(cleaner=cleaner,parent=parent))
        self.setConnect()
