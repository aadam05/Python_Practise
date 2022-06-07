from itertools import count

# Считывание существующего файла, на моем пк чет не работает, особо не закицлился на этом

#-----------------------------
# file = input("Enter file name: ")

# try :
#     text = open(file)
# except :
#     print("Wrong file name")

# Открываем наш тестовый файл
file = open("C:\\Users\\05\\Downloads\\edu\\testText4.txt")


count = 0 # Для подсчета длины нужных нам строк
for lines in file :
    lines = lines.rstrip()
    middle = lines.split()
    
    # Если длина не равна 3 индексам пропускаем 
    # Если первый индекс не равно 'From' пропускаем
    # Это нам нужно для парсинга т.к. в файле много хлама
    if len(middle) < 3 or middle[0] != 'From' : 
        continue
    
    count += 1
    print(middle[1])
    
print('There were', count, 'lines in the file with From as the first word')
