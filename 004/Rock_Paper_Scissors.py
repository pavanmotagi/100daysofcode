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

#Write your code below this line 👇

me = input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n")

if me == "0":
  print(rock)
elif me == "1":
  print(paper)
elif me == "2":
  print(scissors)
else:
  print("Invalid value, please enter 0, 1, or 2.")

print("Computer chose:")

computer = str(random.randint(0,2))

if computer == "0":
  print(rock)
elif computer == "1":
  print(paper)
else:
  print(scissors)

if me == computer:
  print("It's a draw")
elif me == "0":
  if computer == "1":
    print("You lose")
  else:
    print("You win")
elif me == "1":
  if computer == "0":
    print("You win")
  else:
    print("You lose")
else:
  if computer == "0":
    print("You lose")
  else:
    print("You win")