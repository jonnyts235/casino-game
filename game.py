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
    user_input = input("Please select from the following menu choices: \n1: Deposit\n2: Balance\n3: Withdraw\n4: Make a bill payment\n5: Quit \n\nWhat would you like? ")
    if user_input == "50":
      wallet += 50
      print(f"You currently have ${wallet}")
    elif user_input == "100":
      wallet += 100
      print(f"You currently have ${wallet}")
    elif user_input == "150":
      wallet += 150
      print(f"You currently have ${wallet}")
    elif user_input == "200":
      wallet += 200
      print(f"You currently have ${wallet}")
    elif user_input == "250":
      wallet += 250
      print(f"You currently have ${wallet}")
    else: 
      print("That isnt a valid option, please try again")
      user_selection()

    

  def choice_of_color(weights):
    user_choice = input("\nWhat color would you like put bet on?")
    choice_selection = weights.get(user_choice, False)
    if choice_selection == False:
      print("Im sorry that wasn't one of the colours...")
      continue
    else:
      print(f"You picked {choice_selection} no takebacks")
      return choice_selection[1]
      
  def amount_wagered()

  def roulette_function(weights):
      container_list = []

      for (name, weight) in weights.items():
          for _ in range(weights):
              container_list.append(name)

      return np.random.choice(container_list)
  