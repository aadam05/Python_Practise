name = input("Enter file name: ")
try :
    file = open(name)
except :
    print("Wrong file name")

inp = file.read()
inp = inp.rstrip()
print(inp.upper())