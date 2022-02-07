from replit import clear
from art import logo
from random import choice

def blackjack():
  print(logo)

  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  player_cards = []
  computer_cards = []

  def get_a_card(who):
    card = choice(cards)
    if who == "player":
      player_cards.append(card)
    else:
      computer_cards.append(card)

  for _ in range(2):
    get_a_card("player")
    get_a_card("computer")

  print(f"Your cards: {player_cards}")
  print(f"Computer's first card: {computer_cards[0]}")

  get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

  while get_another_card == "y":
    get_another_card = "n"
    get_a_card("player")
    print(f"Your cards: {player_cards}")
    if sum(player_cards) < 21:
      get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    elif 11 in player_cards:
      player_cards.remove(11)
      player_cards.add(1)
      get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

  while sum(computer_cards) < 17:
    get_a_card("computer")

  print(f"Your final hand: {player_cards}")
  print(f"Computer's final hand: {computer_cards}")

  player_sum = sum(player_cards)
  computer_sum = sum(computer_cards)
  
  if player_sum == 21:
    print("You win with a Blackjack!")
  elif computer_sum == 21:
    print("You lose, opponent has Blackjack")
  elif player_sum > 21:
    print("You went over, you lose.")
  elif computer_sum > 21:
    print("Opponent went over, you win.")
  elif player_sum > computer_sum:
    print("You win.")
  elif player_sum < computer_sum:
    print("You lose.")
  else:
    print("It's a draw.")

  go_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

  if go_again == "y":
    clear()
    blackjack()

blackjack()