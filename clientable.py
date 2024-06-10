from PyQt5.QtWidgets import QTableWidgetItem
from dbtablewidget import dbTableWidget

class clientTable(dbTableWidget):
    def __init__(self,cleaner,parent=None):
        header=[
            u'Фамилия',
            u'Имя',
            u'Отчество'
        ]
        dbTableWidget.__init__(self,cleaner=cleaner,parent=parent,header = header)
    def setData(self):
        values = self.getCleaner().getClientCodes()
        self.setRowCount(len(values))
        r=0
        for client in self.getCleaner().getClientList():
            self.setItem(r,0,QTableWidgetItem(client.getSurname()))
            self.setItem(r,1,QTableWidgetItem(client.getName()))
            self.setItem(r,2,QTableWidgetItem(client.getSecname()))
            self.appendRowCode(r,client.getCode())
            r+=1