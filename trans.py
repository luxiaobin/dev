__author__ = 'admin'
import sys, httplib, time
from lxml import etree

HOST ='192.168.10.10:1080'


def do_request(xml_location):
    request = open(xml_location,"r").read()
    webservice = httplib.HTTP(HOST)
    webservice.putrequest("POST", '/other')
    webservice.putheader("Host", HOST)
    webservice.putheader("User-agent", "Yucoder")
    webservice.putheader("Accept-Encoding",'deflate')
    webservice.putheader("Content-length", "%d" % len(request))
    webservice.putheader("Content-type", "text/xml")    
    webservice.endheaders()
    webservice.send(request)
    statuscode, statusmessage, header = webservice.getreply()
    result = webservice.getfile().read()
    print statuscode, statusmessage, header
    #print result
    #root = etree.fromstring(result)
    #textelem = root.find('message/task')
    print result
   
    
do_request("register.xml")
do_request("task.xml")
while True:
    time.sleep(5)
    do_request("status.xml")