# init.py
import random as rnd
def init() -> list[int]:
  """Crée une liste de 4 valeurs aléatoires entre 0 et 8

    Paramètres
    ----------
    Aucun paramètre d'entrée

    Sortie
    -------
    list[int]
        liste de valeurs aléatoire entre 0 et 8 inclus
  """
  combinaison = [rnd.randint(0,8) for i in range(4)]
  return(combinaison)

if __name__ == "__main__": # test
  combinaison = init()
  print(combinaison)
