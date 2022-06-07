hours = input("Enter hours: ")
rate = input("Enter rate: ")

try:    
    hours = float(hours) 
    rate = float(rate)
except:
    print("you typed inccorect value")
    quit()


def computepay(Hours, Rates) :
    if Hours > 40 :
        h = (Hours - 40) * (Rates * 0.5)
        total = Hours * Rates + h 
    else :
        total = Hours * Rates
    return total

total = computepay(hours, rate)
print("Pay", total)

