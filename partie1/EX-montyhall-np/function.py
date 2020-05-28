# importations
import numpy as np
from enum import Enum

# classe Strategy
# > Changer de porte CHANGE = 0
# > Garder la porte de départ KEEP = 1
class Strategy(Enum):
    CHANGE = 0
    KEEP = 1

# fonction play
# prend en argument :
# - la stratégie à appliquer (CHANGE ou KEEP)
# - le nombre d'itérations itr sur lesquelles effectuer la simulation
# et renvoie un tableau numpy de taille itr représentant les gains du joueur
def play(strategy, itr):
    # numérotation des portes
    doors = np.array( [np.array([0, 1, 2]) for i in range(itr)] )
    # "choix" de la bonne porte au hasard
    good_choice = np.array( [np.random.randint(0, 3) for i in range(itr)] )
    # premier choix du joueur au hasard
    first_choice = np.array( [np.random.randint(0, 3) for i in range(itr)] )
    
    # preparation des doors
    doors = np.array( [np.delete(doors[i], first_choice[i]) for i in range(itr)] )
    doors = np.array( [doors[i][np.random.randint(0,2)] if first_choice[i] == good_choice[i]
                       else good_choice[i] for i in range(itr)] )
    
    # préparation liste des seconds choix selon la stratégie
    second_choice = np.array( [doors[i] if (strategy == Strategy.CHANGE)
                               else first_choice[i] for i in range(itr)] )
    # traitement
    result = np.array( [1 if (second_choice[i] == good_choice[i]) else 0
                        for i in range(itr)] )
    return result