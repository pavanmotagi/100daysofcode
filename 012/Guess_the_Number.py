from replit import clear
from random import randint
from art import logo

HARD_LEVEL_TURNS = 5
EASY_LEVEL_TURNS = 10

def game():
  clear()
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  number = randint(1,100)
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

  def take_a_guess(count):
    guess = 0
    while guess != number and count != 0:
      print(f"You have {count} attempts remaining to guess the number")
      count -= 1
      guess = int(input("Make a guess: "))
      if guess > number:
        print("Too high.")
      elif guess < number:
        print("Too low.")
      if guess != number and count != 0:
        print("Guess again.")
    return guess

  if difficulty != "easy" and difficulty != "hard":
    print("Please enter 'easy' or 'hard'")
  else:
    if difficulty == "easy":
      counter = EASY_LEVEL_TURNS
    else:
      counter = HARD_LEVEL_TURNS
    guess = take_a_guess(counter)
    if guess == number:
      print(f"You got it! The number was {number}.")
    else:
      print(f"You've run out of guesses, the number was {number}.")

guess_again = "y"
while guess_again == "y":
  game()
  guess_again = input("Play again? ")