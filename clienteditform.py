from PyQt5.QtWidgets import QLineEdit
from editform import editForm

class clientEditForm(editForm):
    def __init__(self,parent=None,cleaner=None):
        editForm.__init__(self,cleaner=cleaner,parent=parent)
        
        self.__surnameEdit=QLineEdit()
        self.__nameEdit=QLineEdit()
        self.__secnameEdit=QLineEdit()

        self.addLabel(u'Фамилия',0,0)
        self.addNewWidget(self.__surnameEdit,0,1)
        self.addLabel(u'Имя',1,0)
        self.addNewWidget(self.__nameEdit,1,1)
        self.addLabel(u'Отчество',2,0)
        self.addNewWidget(self.__secnameEdit,2,1)

        clientList = self.getCleaner().getClientList()
        if clientList: 
            self.setCurrentCode(clientList[0].getCode())

    def update(self):
        client = self.getCleaner().getClient(self.getCurrentCode())
        if self.getCurrentCode() in self.getCleaner().getClientCodes():
            self.__surnameEdit.setText(client.getSurname())
            self.__nameEdit.setText(client.getName())
            self.__secnameEdit.setText(client.getSecname())

    def editClick(self):
        self.getCleaner().getClient(self.getCurrentCode()).setSurname(self.__surnameEdit.text())
        self.getCleaner().getClient(self.getCurrentCode()).setName(self.__nameEdit.text())
        self.getCleaner().getClient(self.getCurrentCode()).setSecname(self.__secnameEdit.text())

    def newClick(self):
        client=self.getCleaner().newClient()
        self.setCurrentCode(client.getCode())

    def delClick(self):
        self.getCleaner().removeClient(self.getCurrentCode())