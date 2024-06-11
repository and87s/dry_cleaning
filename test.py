from PyQt5.QtWidgets import QApplication
from drycleaning import dryСleaning
from dataxml import dataxml
from clienteditform import clientEditForm as testwidget
import sys

app = QApplication(sys.argv)
cleaner=dryСleaning()
dat1=dataxml(cleaner,'oldfile.xml')
dat1.read()
tw=testwidget(cleaner = cleaner) 
tw.setCurrentCode(1)
tw.show()
sys.exit(app.exec_())