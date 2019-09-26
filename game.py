import numpy as np

wallet = 0

def casino_game():

  weights = {
  'red': 18,
  'green': 1,
  'black': 18
  }

  def play_again():
    user_decision = input("\nWould you like to play again? Yes or No... ").lower()
    if user_decision == 'yes':
      return user_selection()
    elif user_decision == 'no':
      print('Thanks for playing ;)')
    else:
      print('That is not an option, Please give an actual response')
      play_again()


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


  def choice_of_color(weights):
    user_choice = input("\nWhat color would you like put bet on? Green, Red, Black? ").lower()
    choice_selection = weights.get(user_choice, False)
    if choice_selection == False:
      print("Im sorry that wasn't one of the colors...")
      choice_of_color(weights)
    else:
      print(f"You picked {user_choice} no withdraws")
    roulette_function(weights, user_choice)

  def roulette_function(weights, user_choice):
    container_list = []

    for (name, weight) in weights.items():
      for _ in range(weight):
        container_list.append(name)

    outcome = np.random.choice(container_list)
    win_or_loss(outcome, user_choice)

  def win_or_loss(outcome, user_choice):
    global wallet
    if user_choice == outcome:
      wallet *= 2
      print(f"CONGRATS!!! You picked {user_choice}, which was the winning color. ")
    else:
      wallet -= wallet
      print("Sorry your choice wasn't the right one... You're broke")
    print(f"You have ${wallet}")
    play_again()
  user_selection()


casino_game()
