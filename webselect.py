from cleanerwidget import cleanerWidget
from formelement import formElement

class webSelect(cleanerWidget, formElement):
    def __init__(self, cleaner=None, id=None, name=None, cl=None):
        cleanerWidget.__init__(self, cleaner)
        formElement.__init__(self, id, name, cl)
        self.setCurrentValue(None)
    
    def setCurrentValue(self, value):
        self.__currentValue = value
    
    def getCurrentValue(self):
        return self.__currentValue
    
    def __start(self):
        s='<select id="%s" class="form-select %s" name="%s">' %(self.getId(), self.getName(), self.getClass())
        return s

    def appendOption(self,value='', text=''):
        text = text if text else value
        selected = 'selected' if value == self.__currentValue else ''
        s='<option value="%s" %s>%s</option>' % (value, selected, text)
        return s
    
    def setData(self):
        return ''
    
    def update(self):
        return self.__start()+self.setData()+self.__end()
    
    def __end(self):
        return '</select>'