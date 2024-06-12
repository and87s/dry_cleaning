from PyQt5.QtWidgets import QApplication
from drycleaning import dryСleaning
from dataxml import dataxml
from servicepage import servicesPage as testwidget
import sys

app = QApplication(sys.argv)
cleaner=dryСleaning()
dat1=dataxml(cleaner,'oldfile.xml')
dat1.read()
tw=testwidget(cleaner = cleaner) 
#tw.setCurrentCode(2)
tw.show()
sys.exit(app.exec_())