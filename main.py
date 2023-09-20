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

choices = [rock,paper,scissors]

user_input = int(input("Enter  0 for Rock , 1 for Paper and 2 for Scissors: "))
print(choices[user_input])

computer_input = random.randint(0,2)
print("Computer's input: ") 
print(choices[computer_input])

if user_input >= 3 or user_input < 0: 
  print("You typed an invalid number, you lose!") 
elif user_input == 0 and computer_input == 2:
  print("You win!")
elif computer_input == 0 and user_input == 2:
  print("You lose")
elif computer_input > user_input:
  print("You lose")
elif user_input > computer_input:
  print("You win!")
elif computer_input == user_input:
  print("It's a draw")
   