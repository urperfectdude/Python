
def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

replay = int(input("Enter 1 to perform calculation"))

while replay == 1:
    
    num1 = int(input("Enter first num"))

    ask = input("what operation you want to do? ")

    num2 = int(input("Enter second num"))

    if ask == '+':
        print(add(num1,num2))
    elif ask == '-':
        print (sub(num1,num2))
    elif ask == '/':
        print (div(num1,num2))
    elif ask == '*':
        print (mul(num1,num2))
    else :
        print ("wrong input")
    
    replay = int(input("Enter 1 to repeat calculation"))
else:
    print("Thanks for using")


