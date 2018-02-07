import os,requests
from lxml import etree
from xml.dom.minidom import parse


import sys

DML_URL="http://dml.prod.d3nw.net/dml/v2/library"
cus="bigstarz"
key='17C82B0E-94C6-487A-A2E6-A7939BE8C27F'
origin="origin.pof.d3nw.com"

working_dir = 'C:\Users\jdas\Desktop\Python\Selenium_learning\CDN_check'

os.chdir(working_dir)

data = requests.get(DML_URL,headers={'X-DML-API-KEY':key},stream=True)
with open('out.xml','w') as f:
    for d in data:
        f.write(d)

#xml = parse('out.xml')
#formated_xml = xml.toprettyxml()