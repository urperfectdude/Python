coffee_list = {"1":"espressco", "2":"latte","3": "cappuciouno"}

print (f"We have {coffee_list}")
coffee = input("What you would like to have?")

cl_1 = {
    "name": "Espressco Coffee",
    "water": "200ml",
    "milk": "200ml",
    "money": "$0.25",
}

cl_2 = {
    "name": "Latte Coffee",
    "water": "200ml",
    "milk": "200ml",
    "money": "$0.75",
}

cl_3 = {
    "name": "Cappuciono Coffee",
    "water": "200ml",
    "milk": "200ml",
    "money": "$1",
}

if coffee == '1':
    print (cl_1)
elif coffee == '2':
    print (cl_2)
elif coffee == '3':
    print (cl_3)

store = {
    "Water": 2000,
    "milk": 2000,
    "money": 10,
}