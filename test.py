# test.py
def test(CombiUser : list[int], combiOrigin : list[int]) -> list[str]:
  """Donné deux listes : combiUser et combiOrigin, renvoie une liste de Noirs (N) et de Blancs (B)"""
  listNoirBlanc = []
  for i in range(len(CombiUser)):
    if CombiUser[i]==combiOrigin[i]:
      listNoirBlanc.append("N")
    elif CombiUser[i] in combiOrigin:
      listNoirBlanc.append("B")
  return listNoirBlanc
  
if __name__ == "__main__": # test
  combiUser = [1,2,3,4]
  combiOrigin = [1,5,4,6]
  print(test(combiUser,combiOrigin))
