import random

rock ='''
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = ''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
 '''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) '''

ascii_art = [rock, paper, scissor]


def game_start():

    user_raw = input ("Enter your choic 0,1 & 2 for Rock, Paper & Scissor respectively")
    user = int(user_raw)
    

    if user < 3 :
        print ("User Chose"+ascii_art[user])

        computer = random.randint(0,2)
        print ("Computer Chose"+ascii_art[computer])

        if user == computer :
            print ("Its Draw")

        elif user == 0 or computer == 2:
            print ("You Win")

        elif computer == 2 or user == 0:
            print ("You Loose")

        elif user == 0 or computer == 1 :
            print ("You Loose")

        elif user == 1 or computer == 0 :
            print ("You win")

        elif user == 1 or computer == 2:
            print ("You Loose")

        else :
            print ("Its Draw")

        replay_raw = input ("Enter 0 to Replay and 1 to End")
        replay = int(replay_raw)

        while replay == 0:
            print (game_start())

        else :
            print ("Thank You for playing")

    else :
        print ("Invalid Input")
        
print (game_start())



