from cleanerwidget import cleanerWidget
from formelement import formElement

class webInput(cleanerWidget, formElement):
    def __init__(self, cleaner=None, type='', id=None, name=None, cl=None, value=None):
        cleanerWidget.__init__(self, cleaner)
        formElement.__init__(self, id, name, cl)
        self.setType(type)
        self.setValue(value)

    def setType(self, value):
        self.__type = value

    def getType(self):
        return self.__type
    
    def setValue(self, value):
        self.__value = value

    def getValue(self):
        return self.__value
       
    def update(self):
        return '<input type="%s" id="%s" name="%s" class="form-control %s" value="%s">' %(self.__type, self.getId(), self.getName(), self.getClass(), self.__value)