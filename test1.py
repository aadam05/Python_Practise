hours = input("Enter hours: ")
rate = input("Enter rate: ")

try:    
    Hour = float(hours) 
    Rate = float(rate)
except:
    print("you typed inccorect value")
    quit()

if Hour > 40 :
    h = (Hour - 40) * (Rate * 0.5)
    total = Hour * Rate + h 
else :
    total = Hour * Rate
print(total)

