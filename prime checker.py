


flag = True

ans = input("Want to check num? ")

while ans == 'yes' :

    num = int(input("Enter a num "))

    if num > 1:
        for i in range (2,num):
            if (num % i)==0:
                flag = False
                break

    if flag:
        print(" Its a prime")
    else:
        print(" is not a prime")

    ans = input("Want to check once again? ")
