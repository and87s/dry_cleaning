from PyQt5.QtWidgets import QApplication
from drycleaning import dryСleaning
from dataxml import dataxml
from kindservicetable import kindServiceTable
import sys

app = QApplication(sys.argv)
cleaner=dryСleaning()
dat1=dataxml(cleaner,'oldfile.xml')
dat1.read()
tw1=kindServiceTable(cleaner=cleaner)
tw1.show()
sys.exit(app.exec_())