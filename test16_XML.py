import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

numbers = list()

# Игнорим https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "https://py4e-data.dr-chuck.net/comments_1562750.xml"
html = urllib.request.urlopen(url, context=ctx).read()  # Читаем html
xml = ET.fromstring(html)   # Парсим html в XML
value = xml.findall('comments/comment')    # В эту переменную помещаем ноды которые нам нужны


for item in value:
    number = item.find('count').text
    numbers.append(int(number))


print(sum(numbers))