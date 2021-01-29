# test.py
from random import shuffle
def test(CombiUser : list[int], combiOrigin : list[int]) -> list[str]:
  """Donné deux listes : combiUser et combiOrigin, renvoie une liste de Noirs (N) et de Blancs (B), soit dans l'ordre, soit dans un ordre aléatoire (aléatoire par défaut)
  
  Paramètres
    ----------
    CombiUser : liste contenant la combinaison entrée précédemment par l'utilisateur
    combiOrigin : liste contenant la combinasion aléatoire crée par init()

  Sortie
  -------
  list[int]
      liste de Noirs ('N') et de Blancs ('B')
  """
  listNoirBlanc = []
  if len(CombiUser)!=4:
    return listNoirBlanc
  for i in range(4):
    if CombiUser[i]==combiOrigin[i]:
      listNoirBlanc.append("N")
    elif CombiUser[i] in combiOrigin:
      listNoirBlanc.append("B")
  shuffle(listNoirBlanc) # Désactivation possible mais permettant la triche
  return listNoirBlanc
  
if __name__ == "__main__": # test
  combiUser = [1,2,3,4]
  combiOrigin = [1,5,4,6]
  print(test(combiUser,combiOrigin))
