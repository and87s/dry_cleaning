from PyQt5.QtWidgets import QTableWidgetItem
from dbtablewidget import dbTableWidget

class kindServiceTable(dbTableWidget):
    def __init__(self,cleaner,parent=None):
        header=[
            u'Наименование',
            u'Вид услуги',
            u'Цена'
        ]
        dbTableWidget.__init__(self,cleaner=cleaner,parent=parent,header = header)
    def setData(self):
        values = self.getCleaner().getKindServiceCodes()
        self.setRowCount(len(values))
        r=0
        for kindService in self.getCleaner().getKindServiceList():
            self.setItem(r,0,QTableWidgetItem(kindService.getName()))
            self.setItem(r,1,QTableWidgetItem(kindService.getTypeService()))
            self.setItem(r,2,QTableWidgetItem(str(kindService.getPrice())))
            self.appendRowCode(r,kindService.getCode())
            r+=1