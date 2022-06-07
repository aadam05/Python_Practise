score = input("Enter score: ")
try :
    total = float(score)
except :
    print("Wrong value")
    quit()

if total > 1.0 :
    print("The score could be from 0.0 to 1.0")
elif total < 0.0 :
    print("The score could be from 0.0 to 1.0")
elif total >= 0.9 :
    print("A")
elif total >= 0.8 :
    print("B")
elif total >= 0.7 :
    print("C")
elif total >= 0.6 :
    print("D")
elif total < 0.6 :
    print("F")
