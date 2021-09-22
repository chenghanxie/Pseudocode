#Python simple menu - text based adventure game 
#CS 30 
#Chenghan Xie
#Ms. Cotcher
#September 22, 2021
#This is a program that user will enter inputs until the game is over. A game can be over. either you survived or you are killed. Your goal is to survive until the end. You can quit at anytime, Choose wisely.

#Welcome message
print("Welcome to the main menu")
#General actions for the game
actions = ["explore", "combat"]
#Possible actions for the game
possible_explore_actions = ["woods", "grasslands", "lake"]
possible_combat_actions = ["stab it", "shoot it", "punch it"]

#While true loop for the story
while True:
  #Main menu, loop will return to this menu 
  print("Choose one of the two options from below,you can quit the game by typing 'quit' at any second.")
  for initial_choice in actions:
    print(initial_choice)
  user_input = input()
  #Sub menu of explore
  if user_input .lower() == "explore":
    for explore_options in possible_explore_actions:
      print(explore_options)
    user_input1 = input("Choose one out of the three options.\n")
    #Options in explore
    if user_input1 .lower() == "woods":
      print("woods!")
    elif user_input1 .lower() == "grasslands":
      print("grasslands!")
    elif user_input1 .lower() == "lake":
      print("lake!")
    elif user_input1 .lower() == "quit":
      print("Successfully quit!")
      break;
    else:
      print("Invalid actions, please try again.")
  #Sub menu of combat
  elif user_input .lower() == "combat":
    for combat_options in possible_combat_actions:
      print(combat_options)
    user_input2 = input("Choose one out of the three options.\n")
    #Options in combat
    if user_input2 .lower() == "stab it":
      print("stab it!")
    elif user_input2 .lower() == "shoot it":
      print("shoot it!")
    elif user_input2 .lower() == "punch it":
      print("punch it!")
    elif user_input2 .lower() == "quit":
      print("Successfully quit!")
      break;
    else:
      print("Invalid actions, please try again.")
  #Quit option
  elif user_input .lower() == "quit":
    print("Successfully quit!")
    break;
  #Invalid action statement 
  else:
    print("Invalid actions, please try again.")

"""The End"""
