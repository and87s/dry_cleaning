#-*- coding:utf-8 -*-
from drycleaning import Himchistka
from dataxml import dataxml

ras1=Himchistka()
dat1=dataxml(ras1,r'oldfile.xml',r'newfile.xml')
dat1.read()
dat1.write()

for k in ras1.getServiceList():
 
    k.print()
    print(' ')
