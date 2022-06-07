import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url=input("Enter url:")

count=int(input('Enter count:'))
pos=int(input('Enter position:'))-1

urllist=list()

for i in range(count):
    html=urllib.request.urlopen(url)
    soup=BeautifulSoup(html,'html.parser')
    tags=soup('a')
    print('Retrieveing:',url)
    taglist=list()
    for tag in tags:
        y=tag.get('href',None)
        taglist.append(y)

    url=taglist[pos]

    urllist.append(url)

print("Last Url:",urllist[-1])
'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Игнорим https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

length = 0
name = list()
names = 0 
tags = soup('a')
for tag in tags:
    url = tag.get('href', None)
    names = re.findall('known_by_(\w+)', url)
    name.append(names[0])
    length += 1

print(name[length - 1])
'''