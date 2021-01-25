# main.py
import tkinter
from init import *
from test import *
from essai import *
from tkinter import * # GUI
from ToolsPerso import * # outils
class Affichages(tkinter):
    """Affichages tkinter"""
    def Principale(root):
        """Fenêtre affichant la combinasion choisie et le résulata précédent, et permet à l'utilsateur de valider son choix"""
        for i in range(4):
            root.rowconfigure(i,weight=1)
        for j in range(4):
            root.columnconfigure(j,weight=1)
        label = Label(root, text="\/Résultat de l'essai précédent (gris et valeur -1 si vide)\/", font=(10))
        label.grid(row=0,column=0,columnspan=4)

        # Affichage combinaison user
        for i in range(len(CombinaisonUser)):
            valClr = CombinaisonUser[i]
            label = Label(root, text=valClr, bg=couleurs[valClr], relief=SOLID, font=(8))
            label.grid(row=2, column=i,ipadx=75,ipady=75)

        # Affichage combinaison noir et blancs
        for i in range(len(ResultatEssai)):
            valClr = ResultatEssai[i]
            label = Label(root, text=valClr, bg=couleurs[valClr], relief=SOLID, foreground="red", font=(8))
            label.grid(row=1, column=i,ipadx=75,ipady=75)

        # Dernière ligne
        label = Label(root, text="/\Combinaison choisie/\\", font=(10))
        label.grid(row=3,column=1,columnspan=2)
        button = Button(root, text="Valider", command=root.destroy, bg="#6bc55d", activebackground="grey") # bouton vert 
        button.grid(row=3,column=0,ipadx=50,ipady=30)
        button = Button(root, text="Annuler", command=root.destroy, bg="#db2915", activebackground="grey") # bouton rouge
        button.grid(row=3,column=3,ipadx=50,ipady=30)
        root.mainloop()
    def Secondaire(root):
        pass
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
CombinaisonUser = [-1,-1,-1,-1]
ResultatEssai = [-1,-1,-1,-1]
CombinaisonATrouver = init()
couleurs = {-1:"grey","B":"white","N":"black"}
root = Tk()
root.title("Mastermind")
root.geometry("600x600")
Affichages.Principale(root) # Affichage première fenêtre
# programme
nEssais = 0
CombinaisonATrouver = init()
while nEssais<10 and not CombinaisonUser==CombinaisonATrouver: # Boucle jeu
    nEssais+=1
    # print(CombinaisonATrouver) # debug victoire
    CombinaisonUser = essai()
    while CombinaisonUser==-1: # Demande Combinaison
        Tools.suppr(1)
        CombinaisonUser = essai()
    print("Combinaison choisie :",CombinaisonUser)
    ResultatEssai = test(CombinaisonUser,CombinaisonATrouver)
    print("Résultat :",ResultatEssai)
if CombinaisonUser==CombinaisonATrouver: # Si gagné
    print("Bravo, la combinaison était bien",CombinaisonATrouver)
    print("Gagné !")
else:
    print("Pas de chance, la combinaison a trouver était :",CombinaisonATrouver)
    print("Perdu !")