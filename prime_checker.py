
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")  


n = int(input("Check this number: "))
prime_checker(number=n)

replay = input("Do u want to check once again?")

while replay == "yes":
    n = int(input("Check this number: "))

    if isinstance(n,int):
        prime_checker(number=n)
        replay = input("Do u want to check once again?")
    else :
        print ("Wrong Input, Try Again")
        n = int(input("Check this number: "))

    replay = input("Do u want to check once again?")

print ("Thanks For using")


