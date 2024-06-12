from dbcombobox import dbComboBox

class clientCombo(dbComboBox):
    def update(self):
        self.clear()
        for p in self.getCleaner().getClientList():
            self.addItem(p.getCode(),p.getDecription())
        currentClient = self.getCleaner().getService(self.getCurrentRec()).getClient()
        if currentClient:
            self.setCurrentCode(currentClient.getCode())
        else: self.setCurrentIndex(-1)