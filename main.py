# main.py
from init import *
from test import *
from tkinter import * # GUI
from ToolsPerso import * # outils
class fenetreMain:
    def __init__(self): # Premier affichage
        label = Label(self, text="avant")
        label.pack()
    def updateClr(self): # update à chaque choix de couleur
        pass
    def updateTry(self): # update à chaque essai de combinaison
        pass
class SplashScreen(fenetreMain): # Fenetre secondaire
    def __init__(self,parent):
        label = Label(parent, text="test")
        label.pack(padx=5,pady=5)
# Texte d'explication (introduction)
root = Tk()
root.title("Introduction")
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
root = Tk()
root.title("Mastermind")
root.geometry("500x500")
for i in range(4):
    root.rowconfigure(i,weight=1)
for j in range(4):
    root.columnconfigure(j,weight=1)
label = Label(root, text="djfkjdsfjosdfjosdfjsdfdsigfh")
label.grid(row=0,column=0,columnspan=4)
button = Button(root, text="Valider", command=root.destroy, bg="#6bc55d", activebackground="grey") # bouton vert 
button.grid(row=3,column=1,ipadx=20,ipady=20)
button = Button(root, text="Annuler", command=root.destroy, bg="#db2915", activebackground="grey") # bouton rouge
button.grid(row=3,column=2,ipadx=20,ipady=20)
root.mainloop()
nEssais = 0
CombinaisonATrouver = init()
CombinaisonUser = []
while nEssais<10 and not CombinaisonUser==CombinaisonATrouver: # Boucle jeu
    nEssais+=1
    print(CombinaisonATrouver)
    CombinaisonUser = []
    inputU = -1
    for ninput in range(4):
        while inputU==-1:
            try:
                inputU = int(input("Input couleur/valeur "+str(ninput+1)+" : "))  
            except ValueError:
                inputU = -1
                Tools.suppr(1)
        CombinaisonUser.append(inputU)
    print("Combinaison choisie :",CombinaisonUser)
    ResultatEssai = test(CombinaisonUser,CombinaisonATrouver)
    print("Résultat :",ResultatEssai)
if CombinaisonUser==CombinaisonATrouver: # Si gagné
    print("Bravo, la combinaison était bien",CombinaisonATrouver)
    print("Gagné !")
else:
    print("Pas de chance, la combinaison a trouver était :",CombinaisonATrouver)
    print("Perdu !")