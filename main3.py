import os
from drycleaning import dryСleaning
from dataxml import dataxml
from datasql import datasql

ras1=dryСleaning()
ras2=dryСleaning()
dat1=dataxml(ras1,r'oldfile.xml',r'newfile.xml')
dat2=dataxml(ras2,r'oldfile.xml',r'newfile.xml')

dsql1=datasql(ras1,'new.sqlite','new.sqlite')
dsql2=datasql(ras2,'new.sqlite','new.sqlite')

dat1.read()
if os.path.isfile(dsql1.getOut()):os.remove(dsql1.getOut())
dsql1.write()
dsql2.read()
dat2.write()

for k in ras1.getServiceList():
    k.print()
    print(' ')