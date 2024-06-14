from cleanerwidget import cleanerWidget
from clientwebselect import clientWebSelect
from kindservicewebselect import kindServiceWebSelect
from webinput import webInput
from formelement import formElement

class serviceWebForm(cleanerWidget):
    def __init__(self, cleaner = None, code = None) -> None:
        cleanerWidget.__init__(self,cleaner)
        self.setCode(code)
        self.__clientSelect = clientWebSelect(cleaner, 'client')
        self.__kindSelect = kindServiceWebSelect(cleaner, 'kindService')
        self.__countEdit = webInput(cleaner, 'number', 'count')
        
    def setCode(self, code):
        self.__code = code
        
    def update(self):
        if self.__code:
            service = self.getCleaner().getService(int(self.__code))
            if service:

                self.__clientSelect.setCurrentValue(service.getClient().getCode())
                self.__kindSelect.setCurrentValue(service.getKindService().getCode())
                self.__countEdit.setValue(service.getCount())
                inputs=''
                inputs+=self.addRow(self.__clientSelect, "Клиент")
                inputs+=self.addRow(self.__kindSelect, "Услуга")
                inputs+=self.addRow(self.__countEdit, "Количество")

                f="""
                <div class="row py-md-5">
                    <form method="get" action="/">
                    %s
                    <button type="submit" class="btn btn-primary">Сохранить</button>
                </form>""" % (inputs)
                return f
            else: return "Не найден заказ с номером %s" % (int(self.__code))

    def addRow(self, input:formElement, text):
        s = '<div class="mb-3 row"><label for="%s" class="col-sm-2 col-form-label">%s</label><div class="col-sm-10">%s</div></div>' % (input.getName(), text, input.update())
        return s