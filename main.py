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
    ________
---'   _____)____
          _______)
          ________)
         ________)
---.__________)
'''

scissors = '''
    _______
---'   ____)_____
          _______)
       ___________)
      (____)
---.__(___)
'''

gestures = [rock, paper, scissors]

user_choice = input("What do you chose? Type 0 for Rock, 1 for Paper and 2 for Scissors. ")

computer_choice = random.randint(0, 2)