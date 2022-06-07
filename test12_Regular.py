import re

text = open("C:\\Users\\05\\Downloads\\edu\\testTEXT4.txt")
amount = list()
amount1 = list()
total = 0

# НУЖНО ПОСЧИТАТЬ СУММУ ВСЕХ ЧИСЕЛ В ТЕКСТОВОМ ФАЙЛЕ
# НУЖНО ПОСЧИТАТЬ СУММУ ВСЕХ ЧИСЕЛ В ТЕКСТОВОМ ФАЙЛЕ
# НУЖНО ПОСЧИТАТЬ СУММУ ВСЕХ ЧИСЕЛ В ТЕКСТОВОМ ФАЙЛЕ

for lines in text :
    stripped = lines.rstrip()

    # Ищем в тексте все цифры 
    total = re.findall('[0-9]+', stripped)
    
    # Если не сделаем условие то, будет бесконечность  
    if len(total) < 1 :
        continue
    amount.append(total)

index = 0

# У нас двумерный список, все из-за append(), нам надо превратить лист в одномерный
for i in amount :
    
    # Внутри списка есть списки длина которых > 1, если просто сделаем append(), 
    # только 0 индекс будет записан а остальные пропущены  
    if len(i) > 1 :
        for vop in i :
            amount1.append(int(vop))
    
    # Соответственно если длина == 1, то просто вставляем
    else :
        amount1.append(int(i[index]))

print(sum(amount1)) 
    






