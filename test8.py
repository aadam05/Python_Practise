file = open("C:\\Users\\05\\Downloads\\edu\\testTEXT3.txt")
arr = list()
arr1 = list()
arr2 = list()

# Убираем заусенцы в тексте
for lines in file :
    lines = lines.strip()
    lines = lines.split()
    arr.append(lines)

# Не мог отсортировать весь список слов, потому что при итерации каждая строка добавлялась в один индекс, затем второй, третий и четвертый
for count in arr :
    arr1 += count    

# Понимаю что код убогий, но нужно убрать дубликаты слов))
# О боже, что за херню я написал, я знаю что можно облегчить, но как???
for cou in arr1 :
    if cou not in arr2 :
        arr2.append(cou)

arr2.sort()
print(arr2) 