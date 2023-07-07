#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
print(logo)

print("Welcome to the number Guessign Game!\nI'm thinking of a number between 1 and 100.")
choose = input("Choose a difficulty. Type 'easy' or 'hard':")
lives = 10
lives1 = 5
end_loop = True
number = random.randint(1,100)


def rem_lives(guess,number,lives):
    if guess > number:
      print("Too high")
      return lives - 1
    elif guess < number:
      print("Too low")
      return lives - 1
    else:
      print(f"You got it! The answer was {guess}")

      
def rema_lives1(guess,number,lives1):
    if guess > number:
      print("Too high")
      return lives1 - 1
    elif guess < number:
      print("Too low")
      return lives1 - 1
    else:
      print(f"You got it! The answer was {guess}")


def easy(): 
  global end_loop
  global lives
  while end_loop:
    
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess:"))
    lives = rem_lives(guess,number,lives)
    if lives == 0:
      print("Your chances over for guessing, you lose.")
      return 
    else:
      print("Guess again.")

def hard():
  global end_loop
  global lives1
  while end_loop:
    print(f"You have {lives1} attempts remaining to guess the number.")  
    guess = int(input("Make a guess:"))
    lives1 = rema_lives1(guess,number,lives1)
    if lives1 == 0:
      print("Your chances over for guessing,you lose.")
      return
    else:
      print("Guess again.")
      

if choose == "easy":
  easy()
else:
  hard()

#in my code i was unable to get out of the loop 

#approach 2
# from art import logo
# from random import randint

# easy_level = 10
# hard_level = 5

# #check if the guess is same as number
# def check(number,guess,turns):
#   if guess > number:
#     print("Too high")
#     return turns - 1
    
#   elif guess < number:
#     print("Too low")
#     return turns - 1
#   else:
#     print(f"You have chosen the correct number{guess}, You win.")

#difficulty level
# def set_difficulty():
#   choice = input("Choose the difficulty level. Type 'easy' or 'hard':")
#   if choice == "easy":
#     return easy_level
#   else:
#     return hard_level


# def func1():
#   print(logo)
#   print("Welocme to the number Guessing game!")
#   print("I'm thinking to choose a number between 1 to 100.")
#   #choose a random number between 1 to 100
#   number = randint(1,100)
#   turns = set_difficulty()
#   guess = 0
#   while guess != number:
#     print(f"You have {turns} attempts remaining to guess the correct number")
#   #user ll make a guess
#     guess = int(input("Make a guess:"))
#     turns = check(number,guess,turns)
#     if turns == 0:
#       print("You ran out of the chances,You lose.")
#       return 
#     else:
#       print("Guess again.")
      
# func1()





    

      
      
      
  
