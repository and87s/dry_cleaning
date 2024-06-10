#-*- coding:utf-8 -*-
import datetime
import xml.dom.minidom
from data import data

class dataxml(data):
    def read(self):
        dom=xml.dom.minidom.parse(self.getInp())
        dom.normalize()
        for node in dom.childNodes[0].childNodes:
            if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=="client"):
                code,surname,name,secname,regular=0,"","","",""
                for t in node.attributes.items():
                    if t[0]=="code":code=int(t[1])
                    if t[0]=="surname":surname=t[1]
                    if t[0]=="name":name=t[1]
                    if t[0]=="secname":secname=t[1]
                    if t[0]=="regular":regular=int(t[1])
                self.getRas().createClient(code,surname,name,secname,regular)
            if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=="kindService"):
                code,name, typeservice, price =0,"","",0
                for t in node.attributes.items():
                    if t[0]=="code":code=int(t[1])
                    if t[0]=="name":name=t[1]
                    if t[0]=="typeservice":typeservice=t[1]
                    if t[0]=="price":price=t[1]
                self.getRas().createKindService(code,name,typeservice,price)                    
            if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=="service"):
                code,count,dateReception,dateReturn = 0,0,"",""
                for t in node.attributes.items():
                    if t[0]=="code":code=int(t[1])
                    if t[0]=="count":count=int(t[1])
                    if t[0]=="dateReception":dateReception= datetime.datetime.strptime(t[1],'%d.%m.%Y') 
                    if t[0]=="dateReturn":dateReturn=datetime.datetime.strptime(t[1],'%d.%m.%Y')  
                    if t[0]=="client":client=self.getRas().getClient(int(t[1]))
                    if t[0]=="kindService":kindService=self.getRas().getKindService(int(t[1]))
                self.getRas().createService(code,kindService,count,client,dateReception,dateReturn)
    def write(self):
        dom=xml.dom.minidom.Document()
        root=dom.createElement("himchistka")
        dom.appendChild(root)
        for a in self.getRas().getClientList():
            sot=dom.createElement("client")
            sot.setAttribute('code',str(a.getCode()))
            sot.setAttribute('surname',a.getSurname())
            sot.setAttribute('name',a.getName())
            sot.setAttribute('secname',a.getSecname())
            sot.setAttribute('regular',str(a.getRegular()))
            root.appendChild(sot)
        for p in self.getRas().getKindServiceList():
            wtp=dom.createElement("KindService")
            wtp.setAttribute('code',str(p.getCode()))
            wtp.setAttribute('name',p.getName())
            wtp.setAttribute('typeservice',p.getTypeService())
            wtp.setAttribute('price',str(p.getPrice()))
            root.appendChild(wtp)
        for b in self.getRas().getServiceList():
            wor=dom.createElement("Service")
            wor.setAttribute('code',str(b.getCode()))
            wor.setAttribute('kindService',str(b.getKindService().getCode()))
            wor.setAttribute('count',str(b.getCount()))
            wor.setAttribute('dateReception', str(b.getDateReception().strftime('%d.%m.%Y'))) 
            wor.setAttribute('dateReturn',str(b.getDateReturn().strftime('%d.%m.%Y')))
            wor.setAttribute('client',str(b.getClient().getCode()))
            root.appendChild(wor)
        f = open(self.getOut(),"w",encoding='utf-8')
        #f.write(dom.toprettyxml(encoding='utf-8'))
        f.write(dom.toprettyxml())