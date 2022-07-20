import random

print ("Welcome tothe Num Guessing Game! ")
print ("I'm thinking of a num betn 1 - 100 ")

comp = random.randint(1,100)

level = input (" Choose a difficulty type: 'easy' or 'hard' ")

if level == 'easy' :
    turns = 10
    print("You have only 10 attempts for guessing")
else:
    turns = 5
    print ("You have only 5 attempts for guessing")


guess = int(input("Make a guess: "))

while not guess == comp :
    
    if guess > comp :
        print ("Too High")
        turns = turns - 1
        print (f"You have only {turns} attempts for guessing")
        guess = int(input("Make a guess: "))

    elif guess < comp :
        print ("Too Low")
        turns = turns -1
        print (f"You have only {turns} attempts for guessing")
        guess = int(input("Make a guess: "))
        
    else :
        print("Right Guess")
else:
    print("Right Guess")