# main.py
# Texte d'explication
from init import *
from test import *
from tkinter import *
root = Tk()
label = Label(root, text="Bienvenue sur mon jeu de Mastermind !")
label.pack(padx=5,pady=5)
label = Label(root, text="Vous avez 10 essais pour trouver une combinaison de 4 chiffres/couleurs de 0 à 8 inclus")
label.pack(padx=5,pady=5)
label = Label(root, text="A chaque essai, il vous faudra entrer les quatres chiffres (de 0 à 8) que vous pensez les bons")
label.pack(padx=5,pady=5)
label = Label(root, text="Après chaque essai, une liste de noir (N) et blanc (B) vous sera affiché : ")
label.pack(padx=5,pady=5)
label = Label(root, text="- Blanc (B) indique une bonne valeurs/couleurs mais mal placée dans la combinaison")
label.pack(padx=5,pady=5)
label = Label(root, text="- Noir (N) indique une valeur correcte et bien placée")
label.pack(padx=5,pady=5)
label = Label(root, text="Amusez-vous bien !")
label.pack(padx=5,pady=5)
button = Button(root, text="Lancer le jeu", command=root.destroy)
button.pack(pady=10,padx=10)
root.mainloop()
# programme
nEssais = 0
CombinaisonATrouver = init()
CombinaisonUser = []
while nEssais<10 and not CombinaisonUser==CombinaisonATrouver: # Boucle jeu
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