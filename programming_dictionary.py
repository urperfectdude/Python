programming_dictionary = {
    "Bug": "An Error in a program", "Functions":"A piece of code that can be called repeatedly"
}

programming_dictionary["Loop"] = "The repeated action"

print(programming_dictionary)

empty_dictionary = {}
print(programming_dictionary)

for key in programming_dictionary:
    print (key)
    print (programming_dictionary[key])
