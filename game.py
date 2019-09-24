import numpy as np


weights = {
  'red': 18,
  'green': 1,
  'black': 18
}

def casino_game():
    

    def roulette_function(weights):
        container_list = []

        for (name, weight) in weights.items():
            for _ in range(weights):
                container_list.append(name)

        return np.random.choice(container_list)