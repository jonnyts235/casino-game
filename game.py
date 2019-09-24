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
    while True:
      user_input = input("\nHow much money would you like to add to your wallet?")
      wallet += input
    if input != Number.isInteger(input):
      print("Im sorry, must be an integer...")
      continue
    else:
      print(f"You've deposited {wallet} into your wallet")
      return wallet


    def roulette_function(weights):
        container_list = []

        for (name, weight) in weights.items():
            for _ in range(weights):
                container_list.append(name)

        return np.random.choice(container_list)