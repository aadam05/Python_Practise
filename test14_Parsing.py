import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup
import ssl
import re

# Игнорим https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter the URL - ')
# Открываем ссылку и читаем код
html = urllib.request.urlopen(url, context=ctx).read()
# Суп преобразовывает код для удобства
soup = BeautifulSoup(html, 'html.parser')

length = 0
count = 0
total = list()

tags = soup('span')
for tag in tags :
    # Вытаскиваем цифры из строк с помощью регулярок    
    count = re.findall('[0-9]+', str(tag))
    total.append(int(count[0]))
    length += 1

print(sum(total))
print(length)
