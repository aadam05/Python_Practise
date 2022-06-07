text = open("C:\\Users\\05\\Downloads\\edu\\testTEXT4.txt")
emails = dict()

for lines in text :
    line = lines.rstrip()
    words = line.split()
    
    # Убираем варианты строк, где длина строки < 3
    # Также убираем все строки, которые не начинаются с 'From'
    if len(words) < 3 or words[0] != 'From' : 
        continue
    else :
        words = words[1]        # В данной строке есть данные которые нам не нужны, 
                                # оставляем только email

        emails[words] = emails.get(words, 0) + 1       # Добавляем наш email в словарь  
    
maxKey = None
maxValue = None

for key,value in emails.items() :   # Читаем ключ, значение из словаря
    # Если ключ пустой то задаем его, при следующей итерации будет прослеживаться большее значение, нам оно и нужно 
    if maxKey is None or value > maxValue :   
        maxKey = key
        maxValue = value

print(maxKey, maxValue)