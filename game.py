import numpy as np

wallet = 0
def wagering_conditional():
  global wallet
  

def casino_game():

  weights = {
  'red': 18,
  'green': 1,
  'black': 18
  }



  def greeting():
    print("Welcome to Jonny's Roulette")
  greeting()

  def user_selection():
    global wallet
    print("Here are our wallet options\n")
    user_input = input("Please select from the following wallet choices: \n1: $50\n2: $100\n3: $150\n4: $200\n5: $250\n\nWhat would you like? ")
    if user_input == "1":
      wallet += 50
      print(f"Your wallet has ${wallet}\n")
    elif user_input == "2":
      wallet += 100
      print(f"Your wallet has ${wallet}\n")
    elif user_input == "3":
      wallet += 150
      print(f"Your wallet has ${wallet}\n")
    elif user_input == "4":
      wallet += 200
      print(f"Your wallet has ${wallet}\n")
    elif user_input == "5":
      wallet += 250
      print(f"Your wallet has ${wallet}\n")
    else: 
      print("That isnt a valid option, please try again\n")
      user_selection()

    choice_of_color(weights)


    # amount_wagered()

  # def amount_wagered():
  #   global wallet
  #   print("How much would you like to wager?\n")
  #   user_input = input("Please select from the following wager choices: \n1: $50\n2: $100\n3: $150\n4: $200\n5: $250\n\nWhat would you like? ")
  #   while True:
  #     if user_input == "1":
  #       wallet -= 50
  #       if wallet >= 0:
  #         print(f"You wagered $50, now your money is on the table\n")
  #       else:
  #         return amount_wagered()

  #     elif user_input == "2":
  #       wallet -= 100
  #       if wallet >= 0:
  #         print(f"You wagered $100, now your money is on the table\n")
  #       else:
  #         return amount_wagered()

  #     elif user_input == "3":
  #       wallet -= 150
  #       if wallet >= 0:
  #         print(f"You wagered $150, now your money is on the table\n")
  #       else:
  #         return amount_wagered()

  #     elif user_input == "4":
  #       wallet -= 200
  #       if wallet >= 0:
  #         print(f"You wagered $200, now your money is on the table\n")
  #       else:
  #         return amount_wagered()

  #     elif user_input == "5":
  #       wallet -= 250
  #       if wallet >= 0:
  #         print(f"You wagered $250, now your money is on the table\n")
  #       else:
  #         return amount_wagered()

  #     else: 
  #       print("That isnt a valid option, please try again\n")
  #       amount_wagered()

    

  def choice_of_color(weights):
    user_choice = input("\nWhat color would you like put bet on? Green, Red, Black? ").lower()
    choice_selection = weights.get(user_choice, False)
    if choice_selection == False:
      print("Im sorry that wasn't one of the colors...")
      choice_of_color(weights)
    else:
      print(f"You picked {user_choice} no withdraws")
      return choice_selection[1]
    roulette_function(weights, user_choice)

  def roulette_function(weights, user_choice):
    container_list = []

    for (name, weight) in weights.items():
      for _ in range(weights):
        container_list.append(name)

    outcome = np.random.choice(container_list)
    win_or_loss(outcome, user_choice)

  def win_or_loss(outcome, user_choice):
    global wallet
    if user_choice == outcome:
      wallet *= 2
      print(f"CONGRATS!!! You picked {user_choice}, which was the winning color. ")
    else:
      print("Sorry your choice wasn't the right one... You're broke")
  user_selection()

casino_game()