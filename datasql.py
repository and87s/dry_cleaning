#-*- coding:utf-8 -*-
import datetime
import os,xml.dom.minidom
import sqlite3 as db
from data import data

class datasql(data):
    def read(self):
        conn = db.connect(self.getInp())
        curs = conn.cursor()
        curs.execute('select code,surname,name,secname,regular from client')
        data=curs.fetchall()
        for r in data:self.getRas().createClient(r[0],r[1],r[2],r[3])
        curs.execute('select code,name,typeservice,price from kindService')
        data=curs.fetchall()
        for r in data:self.getRas().createKindService(r[0],r[1],r[2],r[3])
        curs.execute('select code,kindService,count,client, dateReception, dateReturn from Service')
        data=curs.fetchall()
        for r in data: self.getRas().createService(r[0],self.getRas().getKindService(int(r[1])),r[2],self.getRas().getClient(int(r[3])),datetime.datetime.strptime(r[4],'%Y-%m-%d %H:%M:%S'),datetime.datetime.strptime(r[5],'%Y-%m-%d %H:%M:%S') )
        conn.close()
    def write(self):
        conn = db.connect(self.getOut())
        curs = conn.cursor()
        curs.executescript(emptydb)
        for a in self.getRas().getClientList():
            curs.execute("insert into client(code,surname,name,secname,regular) values('%s','%s','%s','%s','%s')"%(
                a.getCode(),a.getSurname(),a.getName(),a.getSecname(),a.getRegular()))
        for p in self.getRas().getKindServiceList():
            curs.execute("insert into kindService(code,name,typeservice,price) values('%s','%s','%s','%s')"%(
                p.getCode(),p.getName(),p.getTypeService(),p.getPrice()))
        for b in self.getRas().getServiceList():
            curs.execute("insert into service(code,kindService,count,client,dateReception,dateReturn) values('%s','%s','%s','%s','%s','%s')"%(
                b.getCode(),str(b.getKindService().getCode()),b.getCount(),str(b.getClient().getCode()), b.getDateReception().strftime('%Y-%m-%d %H:%M:%S'),b.getDateReturn().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()   
        conn.close()

    def ap(st,aps=True):                   
        if aps:return "'%s'"%str(st)
        else:return "%s"%str(st)

emptydb = """
PRAGMA foreign_keys = ON;

create table client
(code integer primary key,
surname text,
name text,
secname text,
regular integer);

create table kindService
(code integer primary key,
name text,
typeservice text,
price integer);

create table service 
(code integer primary key,
kindservice integer references kindservice(code) on update cascade on delete set null,
count integer,
client integer references client(code) on update cascade on delete set null,
dateReception text,
dateReturn text);
"""

   


