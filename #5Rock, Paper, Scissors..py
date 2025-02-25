import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, scissors, paper]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if user_choice >=0 and user_choice <=2:
    print(game_images[user_choice])
computer_choice = random.randint(0, 2)
print("Computer chose")
print(game_images[computer_choice])
0

if user_choice >2 or user_choice <0:
    print("You typed invalid number. You lose!")

if user_choice == 0 and computer_choice == 2:
    print("You won")
elif computer_choice ==0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You won!")
elif computer_choice == user_choice:
    print("Draw!")
else:
    print("You typed a wrong number. You lost!")




Hello = input("Press enter...")
print(Hello)


