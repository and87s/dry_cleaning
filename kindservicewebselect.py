from webselect import webSelect

class kindServiceWebSelect(webSelect):
    def __init__(self, cleaner=None, id=None, name=None, cl=None):
        super().__init__(cleaner, id, name, cl)

    def setData(self):
        s=self.appendOption(0, "Выберите значение")
        for client in self.getCleaner().getKindServiceList():
            s+=self.appendOption(client.getCode(), client.getName())
        return s
    