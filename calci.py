
def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

operations = {
    "+",
    "-",
    "*",
    "/"
}

num1 = int(input("Enter first num"))
for symbol in operations:
    print (symbol)
operation_symbol = input("Pick Operator")
num2 = int(input("Enter second num"))

calci_function = operations[operation_symbol]
first_ans = calci_function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {first_ans}")



# replay = int(input("Enter 1 to perform calculation"))

# while replay == 1:
    
#     num1 = int(input("Enter first num"))

#     ask = input("what operation you want to do? ")

#     num2 = int(input("Enter second num"))

#     if ask == '+':
#         print(add(num1,num2))
#     elif ask == '-':
#         print (sub(num1,num2))
#     elif ask == '/':
#         print (div(num1,num2))
#     elif ask == '*':
#         print (mul(num1,num2))
#     else :
#         print ("wrong input")
    
#     replay = int(input("Enter 1 to repeat calculation"))
# else:
#     print("Thanks for using")


# def format_name(f_name, s_name):
#     format_f_name =  (f_name.title())
#     format_l_name =  (s_name.title())

#     return f"{format_f_name} {format_l_name}"

# print (format_name("PrashaNT","NAYak"))

