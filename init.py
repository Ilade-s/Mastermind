# init.py
import random as rnd
def init() -> list[int]:
  combinaison = [rnd.randint(0,8) for i in range(4)]
  return(combinaison)
  
if __name__ == "__main__": # test
  combinaison = init()
  print(combinaison)
