text = open("C:\\Users\\05\\Downloads\\edu\\testTEXT4.txt")
hours = dict()


for lines in text :
    line = lines.rstrip()
    words = line.split()
    
    # Убираем варианты строк, где длина строки < 3
    # Также убираем все строки, которые не начинаются с 'From'
    if len(words) < 3 or words[0] != 'From' : 
        continue
    else :
        words = words[5]        # В данной строке есть данные которые нам не нужны, 
                                # оставляем только email
        letter = words[:2]
        hours[letter] = hours.get(letter, 0) + 1       # Добавляем наш email в словарь  

# Вывод
for value,key in sorted(hours.items()) :
    print(value, key)