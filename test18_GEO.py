import urllib.request, urllib.parse, urllib.error
import json

api_key = '42'
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

address = input('Enter location: ')   # Вводим нужное нам место
parms = dict() 
parms['address'] = address    # Закидваем в словарь адрес и ключ API
parms['key'] = api_key   # Закидваем в словарь адрес и ключ API

# Добавляем данные из словаря в ссылку и кодируем чтобы отправить API
url = serviceurl + urllib.parse.urlencode(parms) 
uh = urllib.request.urlopen(url) # GET данные с API

data = uh.read().decode() # Читаем и декодируем
js = json.loads(data) # Закидываем все в JSON

id = js['results'][0]['place_id']   # Вывод id места
print(id)