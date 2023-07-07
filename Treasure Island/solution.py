input1=input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n')
if input1 == "left":
  input2=input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
  if input2 == "wait":
    input3=input("Choose a door, Red, Yelloe, Blue or anything else")
    if input3 == "Yellow":
      print("You win")
    elif input3 == "Red":
      print("Burned by fire.Game over.")
    elif input3 == "Blue":
      print("Eaten by beasts.Game over.")
    else:
      print("Game over.")
  else:
    print("Attacked by trout.Game over.")
else:
  print("Fall into a hole.Game over")