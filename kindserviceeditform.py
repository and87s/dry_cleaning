from PyQt5.QtWidgets import QLineEdit, QDoubleSpinBox
from editform import editForm

class kindServiceEditForm(editForm):
    def __init__(self,parent=None,cleaner=None):
        editForm.__init__(self,cleaner=cleaner,parent=parent)
        
        self.__nameEdit=QLineEdit()
        self.__typeServiceEdit=QLineEdit()
        self.__priceEdit=QDoubleSpinBox()
        self.__priceEdit.setMaximum(999999999.99)

        self.addLabel(u'Наименование',0,0)
        self.addNewWidget(self.__nameEdit,0,1)
        self.addLabel(u'Вид услуги',1,0)
        self.addNewWidget(self.__typeServiceEdit,1,1)
        self.addLabel(u'Цена',2,0)
        self.addNewWidget(self.__priceEdit,2,1)

        kindServiceList = self.getCleaner().getKindServiceList()
        if kindServiceList: 
            self.setCurrentCode(kindServiceList[0].getCode())

    def update(self):
        kindService = self.getCleaner().getKindService(self.getCurrentCode())
        if self.getCurrentCode() in self.getCleaner().getKindServiceCodes():
            self.__nameEdit.setText(kindService.getName())
            self.__typeServiceEdit.setText(kindService.getTypeService())
            self.__priceEdit.setValue(kindService.getPrice())

    def editClick(self):
        self.getCleaner().getKindService(self.getCurrentCode()).setName(self.__nameEdit.text())
        self.getCleaner().getKindService(self.getCurrentCode()).setTypeService(self.__typeServiceEdit.text())
        self.getCleaner().getKindService(self.getCurrentCode()).setPrice(self.__priceEdit.value())

    def newClick(self):
        kindService=self.getCleaner().newKindService()
        self.setCurrentCode(kindService.getCode())

    def delClick(self):
        self.getCleaner().removeKindService(self.getCurrentCode())