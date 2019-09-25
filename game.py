import numpy as np
def casino_game():

  weights = {
  'red': 18,
  'green': 1,
  'black': 18
  }
  wallet = 0


  def greeting():
    print("Welcome to Jonny's Roulette")

  def user_selection():
    global wallet
    print("Here are our menu options")
    user_input = input("Please select from the following wallet choices: \n1: $50\n2: $100\n3: $150\n4: $200\n5: $250\n\nWhat would you like? ")
    if user_input == "1":
      wallet += 50
      print(f"You currently have ${wallet}")
    elif user_input == "2":
      wallet += 100
      print(f"You currently have ${wallet}")
    elif user_input == "3":
      wallet += 150
      print(f"You currently have ${wallet}")
    elif user_input == "4":
      wallet += 200
      print(f"You currently have ${wallet}")
    elif user_input == "5":
      wallet += 250
      print(f"You currently have ${wallet}")
    else: 
      print("That isnt a valid option, please try again")
      user_selection()
    amount_wagered()

      
  def amount_wagered():
    global wallet
    print("How much would you like to wager?")
    user_input = input("Please select from the following wager choices: \n50: $50\n100: $100\n150: $150\n200: $200\n250: $250\n\nWhat would you like? ")
    if user_input == "0":
      wallet -= 50

      print(f"You wagered ${user_input}, now your money is on the table")
    elif user_input == "1":
      wallet -= 100

      print(f"")
    elif user_input == "2":
      wallet -= 150
      
      print(f"You wagered ${user_input}, now your money is on the table")
    elif user_input == "3":
      wallet -= 200
      
      print(f"You wagered ${user_input}, now your money is on the table")
    elif user_input == "4":
      wallet -= 250
      
      print(f"You wagered ${user_input}, now your money is on the table")
    else: 
      print("That isnt a valid option, please try again")
      amount_wagered()
    choice_of_color(weights)
    

  def choice_of_color(weights):
    user_choice = input("\nWhat color would you like put bet on?")
    choice_selection = weights.get(user_choice, False)
    if choice_selection == False:
      print("Im sorry that wasn't one of the colors...")
      choice_of_color(weights)
    else:
      print(f"You picked {choice_selection} no takebacks")
      return choice_selection[1]
    roulette_function(weights, user_choice, user_choice)

  def roulette_function(weights, user_choice, user_input):
    container_list = []

    for (name, weight) in weights.items():
      for _ in range(weights):
        container_list.append(name)

    outcome = np.random.choice(container_list)
    win_or_loss(outcome, user_choice, user_input)

  def win_or_loss(outcome, user_choice, user_input):
    global wallet
    if user_choice == outcome:
      wallet += user_input * 2
      print(f"CONGRATS!!! You picked {user_choice}, which was the winning color. ")
    else:
      print("Sorry your choice wasn't the right one... You're broke")


casino_game()
