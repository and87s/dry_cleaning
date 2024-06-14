from webtable import webTable
from datetime import datetime

class serviceWebTable(webTable):
    def __init__(self,cleaner=None):
        webTable.__init__(self,cleaner=cleaner,header=["Клиент","Услуга","Количество","Цена","Стоимость", "Дата приема", "Дата возврата"])
    def setData(self):
        s=''
        for service in self.getCleaner().getServiceList():
            s+=self.appendLine(service.getCode(),
                               [service.getClientDesc(),
                                service.getKindService().getName(),
                                service.getCount(),
                                service.getPrice(),
                                service.finalprice(),
                                datetime.strftime(service.getDateReception(),'%d.%m.%Y') if service.getDateReception() else '',
                                datetime.strftime(service.getDateReturn(),'%d.%m.%Y') if service.getDateReturn() else ''])
        return s