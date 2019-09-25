import numpy as np


weights = {
  'red': 18,
  'green': 1,
  'black': 18
}

def casino_game():
  wallet = 0

  def greeting():
    print("Welcome to Jonny's Roulette")

  def user_selection():
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
    wager_amount = input("How much would you like to wager?")
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
        continue
      else:
        print(f"You picked {choice_selection} no takebacks")
        return choice_selection[1]
      roulette_function(weights)

  def roulette_function(weights):
      container_list = []

      for (name, weight) in weights.items():
          for _ in range(weights):
              container_list.append(name)

      return np.random.choice(container_list)


  