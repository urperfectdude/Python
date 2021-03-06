import random

def shuffle(array1, start_range, end_range):
    random_number = random.randint(start_range, end_range)
    n = 0
    i = 0
    array_length = len(array1)
    temp = array1[0]

    while n < random_number:
        if i >= array_length:
            i = 0

        temp = array1[i]
        i += 1
        n += 1
    
    return temp


def validate_string_answer(response, answer):

    if(response[0].lower().count(answer[0].lower()) == 1 and (response.lower() == answer.lower() or len(response) == 1)):
        return True
    else:
        return False

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

def start_game():

    difficulty = input("Choose your game difficulty: Easy(E), Intermediate(I), or Hard(H) ")


    if validate_string_answer(difficulty, 'easy'):
        difficulty = "easy"

    elif validate_string_answer(difficulty, 'intermediate'):
        difficulty = "intermediate"

    else:
        difficulty = "hard"


    input("\nYou are in a jungle chasing hidden treasure and there is cross road in front of you. (Press Enter...)")

    if difficulty == "hard":
        correct_direction = shuffle(['left', 'right'], 0, 5)
    else:
        correct_direction = "left"
    # print(correct_direction)

    direction = input("Which one do you choose to go through? Left(L) or Right(R)?\n")



    if not(validate_string_answer(direction, correct_direction)):
        print("You go for miles, but then you fall into a trap, hole full of spikes.")
        exit("Game Over.")

    input("\nAfter travelling a few miles, you see a river and there is no other way, except going across in order to continue your journey. (Press Enter...)")

    if difficulty == "hard":
        correct_crossing = shuffle(['swim', 'wait'], 0, 5)
    else:
        correct_crossing = "wait"
    # print(correct_crossing)

    crossing = input("How do you go across? Swim(S) through or Wait(W) for a boat?\n")
    


    if not(validate_string_answer(crossing, correct_crossing)):
        print("YOU ARE UNDER ATTACKED!!!\nA bunch of trouts attack you.")
        exit("Game Over.")

    print("\nThat was quite a trip, wasn't it?\n")

    if difficulty == "easy":
        correct_color = "yellow"
    else:
        if correct_crossing == 'swim':
            input("Since you got yourself wet, you decided to stay overnight camping and set the " + colored('fire', 'red') + " up whilst waiting for yourself to get dried up (Press Enter...)\n")
            input("The sun has risen up and you continue your journey... (Press Enter...)")

            if difficulty == "intermediate":
                correct_color = shuffle(['red','blue'], 0, 5)
            else:
                correct_color = shuffle(['yellow','red','blue'], 0, 10)
        else:
            input("The day is still early, so you decided to go through and chase the treasure before the "+ colored('sun', 'yellow') + " sets. (Press Enter)")
            
            if difficulty == "intermediate":
                correct_color = shuffle(['yellow','blue'], 0, 5)
            else:
                correct_color = shuffle(['yellow','red','blue'], 0, 10)

        input("\nAfter succesfully crossing the river and walking for quite sometimes, you are faced with three different doors in front of you. Your treasure is behind one of those doors! (Press Enter...)")

        # print(correct_color)
        door = input("Which door do you choose? Red(R), " + (colored('Blue(B)', 'blue') if difficulty == "intermediate" or difficulty == "hard" else "Blue(B)") + ", or Yellow(Y)?\n")

        if not(validate_string_answer(door, correct_color)):
            if validate_string_answer(door, 'red'):
                print("You are burned by fire.")
                exit("Game Over.")
        elif validate_string_answer(door, 'yellow'):
            print("You are bitten by bees.")
            exit("Game Over.")
        else:
            print("You are eaten by beasts.")
            exit("Game Over")
        

    input("You win! Congratulations. (Press Enter...)")

    replay_raw = input("Enter 0 to replay and 1 to end")
    replay = int(replay_raw)

    while replay ==0:
        print (start_game())
    else :
        print ("Thanks for Playing")

print (start_game())


