from PyQt5.QtWidgets import QVBoxLayout,QLineEdit,QPushButton,QLabel,QSpinBox,QFileDialog,QDoubleSpinBox,QDateEdit
from PyQt5 import QtCore
from editform import editForm
from dbcombobox import dbComboBox
from clientcombo import clientCombo
from kindservicecombo import kindServiceCombo

class serviceEditForm(editForm):
    def __init__(self,parent=None,cleaner=None):
        editForm.__init__(self,cleaner=cleaner,parent=parent)

        self.__ClientCombo = clientCombo(cleaner = cleaner)
        self.addLabel(u'Клиент',0,0)
        self.addNewWidget(self.__ClientCombo,0,1)

        self.__KindServiceCombo = kindServiceCombo(cleaner = cleaner)
        self.addLabel(u'Услуга',1,0)
        self.addNewWidget(self.__KindServiceCombo,1,1)

        self.__CountSpin=QSpinBox()
        self.__CountSpin.setRange(0,1000)
        self.addLabel(u'Количество', 2, 0)
        self.addNewWidget(self.__CountSpin,2,1)

        self.__DateReceptionEdit = QDateEdit()
        self.__DateReceptionEdit.setDisplayFormat('dd.MM.yyyy')
        self.__DateReceptionEdit.setCalendarPopup(True)
        self.addLabel(u'Дата приема', 3, 0)
        self.addNewWidget(self.__DateReceptionEdit,3,1)

        self.__DateReturnEdit = QDateEdit()
        self.__DateReturnEdit.setDisplayFormat('dd.MM.yyyy')
        self.__DateReturnEdit.setCalendarPopup(True)
        self.addLabel(u'Дата возврата', 4, 0)
        self.addNewWidget(self.__DateReturnEdit,4,1)
        if self.getCleaner().getServiceList():
            self.setCurrentCode(self.getCleaner().getServiceList()[0].getCode())

    def update(self):
        if self.getCurrentCode() in self.getCleaner().getServiceCodes():
            self.__ClientCombo.setCurrentRec(self.getCurrentCode())
            self.__KindServiceCombo.setCurrentRec(self.getCurrentCode())
            self.__CountSpin.setValue(self.getCleaner().getService(self.getCurrentCode()).getCount())
            self.__DateReceptionEdit.setDate(self.getCleaner().getService(self.getCurrentCode()).getDateReception())
            self.__DateReturnEdit.setDate(self.getCleaner().getService(self.getCurrentCode()).getDateReturn())
    
    def editClick(self):
        self.getCleaner().getService(self.getCurrentCode()).setClient(self.__ClientCombo.getCurrentCode())
        self.getCleaner().getService(self.getCurrentCode()).setKindService(self.__KindServiceCombo.getCurrentCode())
        self.getCleaner().getService(self.getCurrentCode()).setCount(self.__CountSpin.value())
        self.getCleaner().getService(self.getCurrentCode()).setDateReception(self.__DateReceptionEdit.date())
        self.getCleaner().getService(self.getCurrentCode()).setDateReturn(self.__DateReturnEdit.date())

    def newClick(self):
        b=self.getCleaner().newService()
        self.setCurrentCode(b.getCode())

    def delClick(self):
        self.getCleaner().removeService(self.getCurrentCode())      