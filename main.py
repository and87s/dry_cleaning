#-*- coding:utf-8 -*-
from datetime import datetime
from client import client
from kindservice import kindService
from service import service
from serviceList import ServiceList

serviceList = ServiceList()
k1 = kindService(1,'Химчистка костюма' , 'Чистка текстильных изделий', 1000)
client1 = client(1,'Иванов', 'Иван', 'Иванович')

s1 = service(1,k1, 2, client1, datetime.now().date(), datetime.now().date())
print (s1.getDecription())
serviceList.receptionItem(s1)
serviceList.returnItem(s1)

s2 = service(1,k1, 2, client1, datetime.now().date(), datetime.now().date())
print (s2.getDecription())
serviceList.receptionItem(s2)
serviceList.returnItem(s2)

s3 = s1 = service(1,k1, 2, client1, datetime.now().date(), datetime.now().date())
print (s3.getDecription())
serviceList.receptionItem(s3)
serviceList.returnItem(s3)

s4 = s1 = service(1,k1, 2, client1, datetime.now().date(), datetime.now().date())
print (s4.getDecription())
serviceList.receptionItem(s4)
serviceList.returnItem(s4)