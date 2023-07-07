from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
empty_dic={}

def bidding_func(bidder):
  highest_value = 0
  name = ""
  for bidding in bidder:
    bid_amt = bidder[bidding]
    if bid_amt > highest_value:
      highest_value = bid_amt
      name = bidding
  print(f"The winner is {name} and the higest bid is {highest_value}")
  
while True:
  name = input("Enter your name:")
  bid = int(input("Enter your bidding amount: $"))
  empty_dic[name]=bid
  choice = input("If there are other users who want to bid, Type 'yes' or 'no'?")
  if choice == 'no':
    bidding_func(empty_dic)
    break
  else:
    clear()