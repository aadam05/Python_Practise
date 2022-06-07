largest = None
smallest = None

while True :
    number = input("Enter a numbers: ")
#If we type "Done", our code end
    if number == "done" :
        break

#Catch exceptions when we convert input 
    try :
        number = int(number)
    except :
        print("Invalid input")
        continue

#Find largest number
    if largest is None :
        largest = number
    elif number > largest :
        largest = number

#Find smallest number
    if smallest is None :
        smallest = number
    elif number < smallest :
        smallest = number

print('Maximum is', largest)
print('Minimum is', smallest)










    

