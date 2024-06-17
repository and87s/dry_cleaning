from PyQt5.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QPushButton
from page import page
from servicetable import serviceTable
from serviceeditform import serviceEditForm

class servicesPage(page):
    def __init__(self,cleaner,parent=None):
        page.__init__(self,cleaner=cleaner,parent=parent)

        self.__receptionButton=QPushButton(u"Принять")
        self.__returnButton=QPushButton(u"Выдать")
        self.addButton(self.__receptionButton)
        self.addButton(self.__returnButton)

        self.setTable(serviceTable(cleaner=cleaner,parent=parent))
        self.setForm(serviceEditForm(cleaner=cleaner,parent=parent))
        self.setConnect()

    def setConnect(self):
        page.setConnect(self)
        self.__receptionButton.clicked.connect(self.receptionClik)
        self.__returnButton.clicked.connect(self.returnClik)

    def receptionClik(self):
        self.getForm().receptionClik()
        self.update()

    def returnClik(self):
        self.getForm().returnClik()
        self.update()