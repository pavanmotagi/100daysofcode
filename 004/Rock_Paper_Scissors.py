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

images = [rock,paper,scissors]
me = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))

if me!=0 and me!=1 and me!=2:
  print("You type an invalid input, you lose!")
else:
  print(images[me])
  computer = random.randint(0,2)
  print(f"Computer chose:\n{images[computer]}")

  if me == computer:
    print("It's a draw")
  elif me == 0:
    if computer == 1:
      print("You lose")
    else:
      print("You win")
  elif me == 1:
    if computer == 0:
      print("You win")
    else:
      print("You lose")
  else:
    if computer == 1:
      print("You lose")
    else:
      print("You win")