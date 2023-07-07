# #import both the files
# from art import logo, vs
# from game_data import data
# from random import randint
# from replit import clear



# #global variables
# score = 0
# flag = False

# #choose any random value from the list and print some statement
# def random_value():
#   value = randint(0, 49)
#   return value
  
# def assign():
#   value = random_value()
#   name = data[value]["name"]
#   des = data[value]["description"]
#   country = data[value]["country"]
#   follower = data[value]["follower_count"]
#   return name, des, country, follower


# #compare whose follower_count is more
# def main_func():
#   print(logo)
#   global flag, score
#   while not flag:
#     name_a,des_a,country_a,follower_a = assign()
#     name_b,des_b,country_b,follower_b = assign()
#     print(f"Compare A: {name_a}, {des_a}, {country_a}")
#     print(vs)
#     print(f"Compare B: {name_b}, {des_b}, {country_b}")
    
#     def choose():
#       if follower_a > follower_b:
#         return "A"
#       else:
#         return "B"
  
#     value = choose()
#     user_choice = input("Who has more followers? Type 'A' or 'B':")
#     if user_choice == value:
#       print("You are correct")
#       score += 1
#       clear()
#     else:
#       print("You are wrong")
#       flag = True
#       print("Yo")
#       main_func()
# main_func()


# #compare both and a and b and if the value chosen by us is coorect then the game ll go on until we make mistake and everytime for correct ans increase the score

  
#i had almost solved the problem but could nt be able to solve the part where it would reload and change the value of previus correct answer as the first choice and continue the game

#Aprrocach 2
from art import logo,vs
from game_data import data
from replit import clear
import random
#Display art

print(logo)
score = 0
account_b = random.choice(data)
#Generate random account data
flag = False
while not flag:
  def accountable_data(account):
    name = account["name"]
    des = account["description"]
    country = account["country"]
    return f"{name}, a {des}, from {country}"
  
  account_a = account_b
  account_b = random.choice(data)
  
  while account_a == account_b:
    account_b = random.choice(data)
  
  
  #Format the account data into printable format
  
  print(f"Compare A: {accountable_data(account_a)}")
  print(vs)
  print(f"Against B: {accountable_data(account_b)}")
  
  #take guess from user
  guess = input("Who has more followers? Type 'A' or 'B':").lower()
  
  #check if user guess is right
  def check(guess,a_follower,b_follower):
    if a_follower > b_follower:
      return guess == "a"
    else:
      return guess == "b"
  
  a_follower = account_a["follower_count"]
  b_follower = account_b["follower_count"]
  clear()
  print(logo)
  is_correct = check(guess,a_follower,b_follower)
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    flag = True
    print(f"Sorry, that's wrong. Final score: {score}")