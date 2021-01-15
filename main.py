# main.py
# Texte d'explication
from init import *
from test import *

print("Bienvenue sur mon jeu de Mastermind !")
print("Vous avez 10 essais pour trouver une combinaison de 4 chiffres/couleurs de 0 à 8 inclus")
print("A chaque essai, il vous faudra entrer les quatres chiffres (de 0 à 8) que vous pensez les bons")
print("Après chaque essai, une liste de noir (N) et blanc (B) vous sera affiché : ")
print("\t- Blanc (B) indique une bonne valeurs/couleurs mais mal placée dans la combinaison")
print("\t- Noir (N) indique une valeur correcte et bien placée")
print("\a") ; print("\t\tAmusez-vous bien !")
input("Entrée pour commencer le jeu...")
# programme
nEssais = 0
CombinaisonATrouver = init()
CombinaisonUser = []
while nEssais<10 or CombinaisonUser==CombinaisonATrouver: # Boucle jeu
    nEssais+=1
    print(CombinaisonATrouver)
    CombinaisonUser = []
    for ninput in range(4):
        CombinaisonUser.append(int(input("Input couleur/valeur "+str(ninput+1)+" : ")))
    print("Combinaison choisie :",CombinaisonUser)
    ResultatEssai = test(CombinaisonUser,CombinaisonATrouver)
    print("Résultat :",ResultatEssai)
if CombinaisonUser==CombinaisonATrouver: # Si gagné
    print("Bravo, la combinaison était bien",CombinaisonATrouver)
    print("Gagné !")
else:
    print("Pas de chance, la combinaison a trouver était :",CombinaisonATrouver)
    print("Perdu !")