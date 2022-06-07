# Считывание существующего файла, на моем пк чет не работает, особо не закицлился на этом

#-----------------------------
# file = input("Enter file name: ")

# try :
#     text = open(file)
# except :
#     print("Wrong file name")

# Открываем наш тестовый файл
file = open("C:\\Users\\05\\Downloads\\edu\\testText2.txt")
arr = list()

# Читаем файл
for lines in file :
    lines = lines.strip()    # Убираем whitespaces
    if lines.startswith('X-DSPAM-Confidence: ') :       
        lines = lines.replace('X-DSPAM-Confidence: ', '')      # Заменяем каракули на пустую строку
        lines = float(lines) 
        arr.append(lines)    

### Типо функции sum для листов, но сам написал свою потому что autograder в coursera требовал не использовать sum
i = 0
for count in arr :
    i += count 

print("Average spam confidence:", i / len(arr))    # Считываем среднее арифметическое 
