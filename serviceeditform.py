from PyQt5.QtWidgets import QVBoxLayout,QLineEdit,QPushButton,QLabel,QSpinBox,QFileDialog,QDoubleSpinBox,QDateEdit
from PyQt5 import QtCore
from PyQt5 import QtGui
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

        self.__DateReceptionEdit = QLineEdit()
        #self.__DateReceptionEdit.setDisplayFormat('dd.MM.yyyy')
        #self.__DateReceptionEdit.setCalendarPopup(True)
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
        self.__ClientCombo.setCurrentIndex(-1)
        self.__KindServiceCombo.setCurrentIndex(-1)
        self.__CountSpin.clear()

        #self.__DateReceptionEdit.setSpecialValueText('')
        #self.__DateReceptionEdit.setDate(self.__DateReceptionEdit.minimumDate())
        self.__DateReceptionEdit.setClearButtonEnabled(True)
                
        self.__DateReturnEdit.setSpecialValueText('')
        self.__DateReturnEdit.setDate(self.__DateReturnEdit.minimumDate())

        #self.__DateReceptionEdit.clear()
        #self.__DateReceptionEdit.findChild(QLineEdit).setText('')
        
        #self.__DateReturnEdit.clear()
        #self.__DateReturnEdit.findChild(QLineEdit).setText('')
     
        if self.getCurrentCode() in self.getCleaner().getServiceCodes():
            self.__ClientCombo.setCurrentRec(self.getCurrentCode())
            self.__KindServiceCombo.setCurrentRec(self.getCurrentCode())
            self.__CountSpin.setValue(self.getCleaner().getService(self.getCurrentCode()).getCount())
            dateReception = self.getCleaner().getService(self.getCurrentCode()).getDateReception()
            dateReturn= self.getCleaner().getService(self.getCurrentCode()).getDateReturn()

            if dateReception:
                self.__DateReceptionEdit.setText(dateReception.toString('dd-MM-yyyy'))
            #if dateReception: 
            #    self.__DateReceptionEdit.setDate(dateReception)
            if dateReturn: 
                self.__DateReturnEdit.setDate(dateReturn)
                
    def editClick(self):
        c = self.getCleaner().getClient(self.__ClientCombo.getCurrentCode())
        self.getCleaner().getService(self.getCurrentCode()).setClient(c)

        k = self.getCleaner().getKindService(self.__KindServiceCombo.getCurrentCode())
        self.getCleaner().getService(self.getCurrentCode()).setKindService(k)
        self.getCleaner().getService(self.getCurrentCode()).setCount(self.__CountSpin.value())

        QDateReception = self.__DateReceptionEdit.selectedText()

        #QDateReception = self.__DateReceptionEdit.date()
        #if not QDateReception == self.__DateReceptionEdit.minimumDate():
            #self.getCleaner().getService(self.getCurrentCode()).setDateReception(QDateReception.toPyDate())

        QDateReturn = self.__DateReturnEdit.date()
        if not QDateReturn == self.__DateReceptionEdit.minimumDate():
            self.getCleaner().getService(self.getCurrentCode()).setDateReturn(QDateReturn.toPyDate())

    def newClick(self):
        b=self.getCleaner().newService("",0,"",None,None)
        self.setCurrentCode(b.getCode())

    def delClick(self):
        self.getCleaner().removeService(self.getCleaner().getService(self.getCurrentCode()))      