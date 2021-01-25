import random
import sys
import ctypes # Pour lancement dans console IDLE python (support suppression de texte)
from tkinter import * # GUI
try: # Fonctionnement suppr() sous windows
    kernel32 = ctypes.windll.kernel32 # IDLE suppression
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7) # IDLE suppression
except: pass
class Tools:
    """Outils personnels pour routines :
        - suppression de lignes : suppr(n)
        - conversion nombre en lettre : nbr_abc(n)
        - conversion lettre en nombre : abc_nbr(lettre)
        - Valeur absolue d'un nombre : ValeurAbsolue(n)
        - Outil de probabilité : Proba(n)
        - Test nombre pair ou impair : Pair(n)"""
    def suppr(nlignes: int) -> None:
        """Supprime n lignes de la console"""
        for i in range(nlignes):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
    def nbr_abc(n: int) -> str:
        """Renvoie la lettre à la position n correspondante dans l'alphabet"""
        abc_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        return(abc_list[n-1])
    def abc_nbr(a: str) -> int:
        """Renvoie la position n de la lettre dans l'alphabet"""
        abc_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        return(abc_list.index(a)+1)
    def ValeurAbsolue(n: int) -> int: # Revoie valeur absolue de n
        """Retourne la valeur absolue (positive) de n"""
        if n<0: return(-(n))
        else: return(n)
    def Proba(n: int) -> bool:
        """Permet d'ajouter des conditions de probabilité :
            - n : Nombre entre 1 et 100 : %age de chance
            - sortie : True ou False"""
        tirage = random.randint(1,100)
        if tirage<=n: return(True)
        else: return(False)
    def Pair(n: int) -> bool:
        """Donné un nombre positif entier n, renvoie si il est pair ou non""" 
        nBin = bin(n)
        if nBin[len(nBin)-1]=="0": return(True)
        else: return(False)