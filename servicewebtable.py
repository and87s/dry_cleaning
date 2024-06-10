from webtable import webTable

class serviceWebTable(webTable):
    def __init__(self,cleaner=None):
        webTable.__init__(self,cleaner=cleaner,header=[u'Клиент',u'Услуга',u'Количество',u'Цена',u'Стоимость'])
    def setData(self):
        s=''
        for service in self.getCleaner().getServiceList():
            s+=self.appendLine(service.getCode(),[service.getClient().getDecription(),service.getKindService().getName(),service.getCount(),service.getPrice(),service.finalprice()])
        return s