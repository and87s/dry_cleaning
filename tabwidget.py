from PyQt5.QtWidgets import QTabWidget
import sys,os
from servicepage import servicesPage
from clientpage import clientPage
from kindservicepage import kindServicePage

class tabWidget(QTabWidget):
    def __init__(self,cleaner,parent=None):
        QTabWidget.__init__(self,parent)
        self.__servicePage=servicesPage(cleaner=cleaner)
        self.addTab(self.__servicePage,u"Услуги")
        self.__clientPage=clientPage(cleaner=cleaner)
        self.addTab(self.__clientPage,u"Клиенты")
        self.__kindServicePage=kindServicePage(cleaner=cleaner)
        self.addTab(self.__kindServicePage,u"Виды услуг")
        self.currentChanged.connect(self.update)
    def update(self):
        self.__servicePage.update()
        self.__clientPage.update()
        self.__kindServicePage.update()