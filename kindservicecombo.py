from dbcombobox import dbComboBox

class kindServiceCombo(dbComboBox):
    def update(self):
        self.clear()
        for p in self.getCleaner().getKindServiceList():
            self.addItem(p.getCode(),p.getName())
        currentKindService = self.getCleaner().getService(self.getCurrentRec()).getKindService()
        if currentKindService:
            self.setCurrentCode(currentKindService.getCode())