import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Игнорим https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://py4e-data.dr-chuck.net/comments_1562751.json'
heap = urllib.request.urlopen(url, context=ctx).read()
data = json.loads(heap)   # Преобразуем в JSON
nodes = data["comments"]   # Убираем лишнее

numbers = list()
index = 0

for item in nodes:
    num = item["count"]   # Ищем значение типов count 
    numbers.append(int(num))
    index += 1

print(sum(numbers))