from page import page
from servicetable import serviceTable
from serviceeditform import serviceEditForm

class servicesPage(page):
    def __init__(self,cleaner,parent=None):
        page.__init__(self,cleaner=cleaner,parent=parent)
        self.setTable(serviceTable(cleaner=cleaner,parent=parent))
        self.setForm(serviceEditForm(cleaner=cleaner,parent=parent))
        self.setConnect()