from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bids = {}
other_bidders = "yes"
while other_bidders == "yes":
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bids[name] = bid
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n")
  clear()

print(bids)
highest_bid = 0
for bidder in bids:
  if (bids[bidder] > highest_bid):
    highest_bid = bids[bidder]
    highest_bid_by = bidder
print(f"The winner is {highest_bid_by} with a bid of ${highest_bid}")