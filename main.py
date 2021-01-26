# Importation dépendances
from init import *
from test import *
from essai import *
from tkinter import *  # GUI
from ToolsPerso import * # outils
from functools import partial # pour commande avec args tkinter

nEssais = 0
CombinaisonATrouver = init()
def TransitionAffichages(affPrincipal: bool, Données=None):
    """Action boutons pour changements de fenêtre : Efface tout les éléments de la fenetre"""
    for w in root.winfo_children():
        w.destroy()
    root.pack_propagate(0)
    if affPrincipal:    
        Affichage.Secondaire(root) # Affichage seconde fenêtre
    else:
        if Données==None: # Récupération données si présentes
            Affichage.CombinaisonUser = Données
        Affichage.Principale(root) # Affichage première fenêtre  
def FinDePartie():
    """Fonction fille de FinDeTour, renvoie un tuple (Fin?, Gagné?), deux booléens"""
    if Affichage.Combinaison==CombinaisonATrouver: # Victoire
        return(True, True)
    if nEssais==10: # Défaite
        return(True, False)
    else: # Partie pas terminée
        return(False, False)
def FinDeTour():
    """Déclenchée par le bouton de validation de la fenêtre principale"""

    pass
class Affichages:
    """Affichages tkinter"""
    def __init__(self) -> None:
        self.CombinaisonUser = []
    def Intro(root):
        """Fenêtre avec texte d'introduction"""
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
    def Principale(root):
        """Fenêtre affichant la combinaison choisie et le résultat précédent, et permet à l'utilsateur de valider son choix"""
        root.title("Mastermind : fenêtre principale")
        for i in range(4):
            root.rowconfigure(i,weight=1)
        for j in range(4):
            root.columnconfigure(j,weight=1)
        label = Label(root, text="\/Résultat de l'essai précédent (gris et valeur -1 si vide)\/", font=(10))
        label.grid(row=0,column=0,columnspan=4)
        # Affichage combinaison user
        for i in range(len(CombinaisonUser)):
            valClr = CombinaisonUser[i]
            label = Label(root, text=valClr, bg=couleurs[valClr], relief=RAISED, font=(8))
            label.grid(row=2, column=i,ipadx=75,ipady=75)
        # Affichage combinaison noir et blancs
        for i in range(len(ResultatEssai)):
            valClr = ResultatEssai[i]
            label = Label(root, text=valClr, bg=couleurs[valClr], relief=RAISED, foreground="red", font=(8))
            label.grid(row=1, column=i,ipadx=75,ipady=75)
        # Dernière ligne
        label = Button(root, text="/\Choisir votre combinaison/\\", font=(10), bg="#4d99c7", command=partial(TransitionAffichages, True))
        label.grid(row=3,column=1,columnspan=2,ipadx=40,ipady=20)
        button = Button(root, text="Valider", command=root.destroy, bg="#6bc55d", activebackground="grey") # bouton vert 
        button.grid(row=3,column=0,ipadx=50,ipady=30)
        button = Button(root, text="Annuler", command=root.destroy, bg="#db2915", activebackground="grey") # bouton rouge
        button.grid(row=3,column=3,ipadx=50,ipady=30)
        root.mainloop()
    def Secondaire(root):
        CombUser = [-1,-1,-1,-1]
        root.title("Mastermind : choix combinaison")
        for i in range(5):
            root.rowconfigure(i,weight=1)
        for j in range(3):
            root.columnconfigure(j,weight=1)
        # Texte intro
        label = Label(root, text="Cliquez sur quatres couleurs pour choisir votre combinaison :", font=(10))
        label.grid(column=0,row=0, columnspan=3)
        # Boutons couleurs pour entrer la combinaison
        for l in range(3):
            for c in range(3):
                valClr = c+3*l
                button = Button(root, text=str(valClr), bg=couleurs[valClr], font=(10))
                button.grid(row=1+l, column=c,ipadx=70,ipady=50)
        # Affichages apercu combinaison entrée
        StrComb = StringVar(root, value=Tools.ListToStr(CombUser))
        label = Label(root, textvariable=StrComb, foreground="red", font=(20))
        label.grid(row=4, column=1)
        # Boutons validation et annulation
        button = Button(root, text="Valider", bg="#6bc55d", command=partial(TransitionAffichages, False, CombUser), font=(10))
        button.grid(row=4, column=0,ipadx=50,ipady=30)
        button = Button(root, text="Annuler", bg="#db2915", command=partial(TransitionAffichages, False, None),font=(10))
        button.grid(row=4, column=2,ipadx=50,ipady=30)
# Texte d'explication (introduction)
root = Tk()
Affichage = Affichages
Affichage.Intro(root)
# programme
CombinaisonUser = [-1,-1,-1,-1]
ResultatEssai = [-1,-1,-1,-1]
CombinaisonATrouver = init()
couleurs = {-1:"grey","B":"white","N":"black"\
    ,0:"red",1:"yellow",2:"orange",3:"blue",4:"green",5:"white",6:"pink",7:"purple",8:"#00ffec"}
root = Tk()
root.geometry("600x600")
Affichage.Principale(root) # Affichage première fenêtre
"""
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
"""