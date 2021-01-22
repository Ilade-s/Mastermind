# init.py
import random as rnd
def init() -> list[int]:
  """Crée une liste de 4 valeurs aléatoires entre 0 et 8"""
  combinaison = [rnd.randint(0,8) for i in range(4)]
  return(combinaison)

if __name__ == "__main__": # test
  combinaison = init()
  print(combinaison)
