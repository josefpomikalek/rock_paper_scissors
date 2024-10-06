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

game_is_on = True

while game_is_on:
    print()
    user_choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper and 2 for Scissors. "))
    print()

    if user_choice > 2 or user_choice < 0:
        print("You typed an invalid number. You lose!")
    else:
        print("You chose:")
        print(gestures[user_choice])

        computer_choice = random.randint(0, 2)
        print()
        print("Computer chose:")
        print(gestures[computer_choice])

        if user_choice == computer_choice:
            print("It's a draw!")
        elif user_choice == 0 and computer_choice == 1:
            print("You lose!")
        elif user_choice == 0 and computer_choice == 2:       
            print("You win!")
        elif user_choice == 1 and computer_choice == 0:
            print("You win!")
        elif user_choice == 1 and computer_choice == 2:
            print("You lose!")
        elif user_choice == 2 and computer_choice == 0:
            print("You lose!")
        elif user_choice == 2 and computer_choice == 1:
            print("You win!")
    print()
    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if play_again == "n":
        print("Thank you for playing my game. Bye!")
        game_is_on = False