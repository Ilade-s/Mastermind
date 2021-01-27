# Importation dépendances
from init import *
from test import *
from essai import *
from tkinter import *  # GUI
from ToolsPerso import * # outils
from functools import partial # pour commande avec args tkinter
# programme
CombinaisonATrouver = init()
def CompleterResEssai(ResEssai: list):
    """Compléte la liste ResultatEssai si sa taille est inférieure à 4"""
    while len(ResEssai)<4:
        ResEssai.append(-1)
    return(ResEssai)
def TransitionAffichages(affPrincipal: bool, Données=None):
    """Action boutons pour changements de fenêtre : Efface tout les éléments de la fenetre"""
    for w in root.winfo_children():
        w.destroy()
    root.pack_propagate(0)
    if affPrincipal:    
        Affichage.Secondaire() # Affichage seconde fenêtre
    else:
        if Données!=None: # Récupération données si présentes
            Affichage.CombinaisonUser = Données
        Affichage.Principale() # Affichage première fenêtre  
def FinDePartie() -> tuple:
    """Fonction fille de FinDeTour, renvoie un tuple (Fin?, Gagné?), deux booléens"""
    if Affichage.CombinaisonUser==CombinaisonATrouver: # Victoire
        return(True, True)
    if Affichage.nEssais==10: # Défaite
        return(True, False)
    else: # Partie pas terminée
        return(False, False)
class Affichages: # Les différentes fenêtres et les variables nécessaires
    """Affichages tkinter"""
    def __init__(self) -> None:
        self.CombinaisonUser = []
        self.ResultatEssai = [-1,-1,-1,-1]
        self.nEssais = 0
    def Intro(self):
        """Fenêtre avec texte d'introduction"""
        root.title("Introduction")
        label = Label(root, text="Bienvenue sur mon jeu de Mastermind !")
        label.pack(padx=5,pady=5)
        label = Label(root, text="Vous avez 10 essais pour trouver une combinaison de 4 chiffres/couleurs de 0 à 8 inclus")
        label.pack(padx=5,pady=5)
        label = Label(root, text="A chaque essai, il faudra cliquer sur 'Choisir votre combinaison', puis cliquer sur vos quatre couleurs")
        label.pack(padx=5,pady=5)
        label = Label(root, text="Après chaque essai, une liste de noir (N) et blanc (B) vous sera affiché, ainsi que votre combinaison précédente : ")
        label.pack(padx=5,pady=5)
        label = Label(root, text="- Blanc (B) indique une bonne valeur/couleur mais mal placée dans la combinaison")
        label.pack(padx=5,pady=5)
        label = Label(root, text="- Noir (N) indique une valeur/couleur correcte et bien placée")
        label.pack(padx=5,pady=5)
        label = Label(root, text="Amusez-vous bien !")
        label.pack(padx=5,pady=5)
        button = Button(root, text="Lancer le jeu", command=root.destroy)
        button.pack(pady=10,padx=10)
        root.mainloop()
    def Principale(self):
        def ButtonCancel():
            """Réinitialisation par clic bouton annuler"""
            Affichage.CombinaisonUser = [-1,-1,-1,-1]
            Affichage.Principale() # Mise à jour
        def ButtonValider():
            """Changement de tour avec bouton valider"""
            ResultatFpartie = FinDePartie()
            if ResultatFpartie[0]: # Partie terminée
                if ResultatFpartie[1]: # Victoire
                    Affichage.EcranVictoire()
                else: # Défaite
                    Affichage.EcranDefaite()
            else: # Partie pas terminée
                self.nEssais+=1
                Affichage.ResultatEssai = CompleterResEssai(test(Affichage.CombinaisonUser, CombinaisonATrouver))
                for i in range(len(self.ResultatEssai)):
                    valClr = self.ResultatEssai[i]
                    label = Label(root, text=valClr, bg=couleurs[valClr], relief=RAISED, foreground="red", font=(8))
                    label.grid(row=1, column=i,ipadx=75,ipady=75)
                label = Label(root, text="Il vous reste "+str(10-Affichage.nEssais)+" essais restants", font=(10))
                label.grid(row=0,column=0,columnspan=4)
        """Fenêtre affichant la combinaison choisie et le résultat précédent, et permet à l'utilsateur de valider son choix"""
        root.title("Mastermind : fenêtre principale")
        for i in range(4):
            root.rowconfigure(i,weight=1)
        for j in range(4):
            root.columnconfigure(j,weight=1)
        label = Label(root, text="Il vous reste "+str(10-Affichage.nEssais)+" essais restants", font=(10))
        label.grid(row=0,column=0,columnspan=4)
        # Affichage combinaison user
        for i in range(len(Affichage.CombinaisonUser)):
            valClr = Affichage.CombinaisonUser[i]
            label = Label(root, text=valClr, bg=couleurs[valClr], relief=RAISED, font=(8))
            label.grid(row=2, column=i,ipadx=75,ipady=75)
        # Affichage combinaison noir et blancs
        for i in range(len(self.ResultatEssai)):
            valClr = self.ResultatEssai[i]
            label = Label(root, text=valClr, bg=couleurs[valClr], relief=RAISED, foreground="red", font=(8))
            label.grid(row=1, column=i,ipadx=75,ipady=75)
        # Dernière ligne
        label = Button(root, text="/\Choisir votre combinaison/\\", font=(10), bg="#4d99c7", command=partial(TransitionAffichages, True))
        label.grid(row=3,column=1,columnspan=2,ipadx=40,ipady=20)
        button = Button(root, text="Valider", command=ButtonValider, bg="#6bc55d", activebackground="grey") # bouton vert 
        button.grid(row=3,column=0,ipadx=50,ipady=30)
        button = Button(root, text="Annuler", command=ButtonCancel, bg="#db2915", activebackground="grey") # bouton rouge
        button.grid(row=3,column=3,ipadx=50,ipady=30)
    def Secondaire(self):
        """Fenêtre permettant de choisir la combinaison à essayer"""
        def ClicClr(clr):
            """Ajoute la couleur choisie (selon le bouton) à CombUser si possible et met à jour les textes"""
            if len(CombUser)<4:    
                CombUser.append(clr)
                labelInfo.configure(text="Encore "+str(4-len(CombUser))+" couleurs à choisir :")
            if len(CombUser)==4:
                labelInfo.configure(text="Vous pouvez maintenant valider")
            labelAprecu.configure(text=Tools.ListToStr(CombUser))
        CombUser = []
        root.title("Mastermind : choix combinaison")
        for i in range(5):
            root.rowconfigure(i,weight=1)
        for j in range(3):
            root.columnconfigure(j,weight=1)
        # Texte intro
        labelInfo = Label(root, text="Encore "+str(4-len(CombUser))+" couleurs à choisir :", font=(10))
        labelInfo.grid(column=0,row=0, columnspan=3)
        # Boutons couleurs pour entrer la combinaison
        for l in range(3):
            for c in range(3):
                valClr = c+3*l
                button = Button(root, text=str(valClr), bg=couleurs[valClr], font=(10), command=partial(ClicClr, valClr))
                button.grid(row=1+l, column=c,ipadx=70,ipady=50)
        # Affichages apercu combinaison entrée
        labelAprecu = Label(root, text=Tools.ListToStr(CombUser), foreground="red", font=(20))
        labelAprecu.grid(row=4, column=1)
        # Boutons validation et annulation
        button = Button(root, text="Valider", bg="#6bc55d", command=partial(TransitionAffichages, False, CombUser), font=(10))
        button.grid(row=4, column=0,ipadx=50,ipady=30)
        button = Button(root, text="Annuler", bg="#db2915", command=partial(TransitionAffichages, False, None),font=(10))
        button.grid(row=4, column=2,ipadx=50,ipady=30)
    def EcranVictoire(self):
        """Ecran de victoire à afficher"""
        for w in root.winfo_children():
            w.destroy()
            root.pack_propagate(0)
        root.title("Mastermind : Victoire")
        for i in range(4):
            root.rowconfigure(i,weight=1)
        for i in range(4):    
            root.columnconfigure(i,weight=1)
        label = Label(root, text="Bravo, vous avez trouvé la bonne combinaison !", font=(10))
        label.grid(row=0,column=0,columnspan=4)
        label = Label(root, text="Combinaison trouvée :", font=(10))
        label.grid(row=1,column=0,columnspan=4)
        # Affichage combinaison user
        for i in range(4):
            valClr = Affichage.CombinaisonUser[i]
            label = Label(root, text=valClr, bg=couleurs[valClr], relief=RAISED, font=(8))
            label.grid(row=2, column=i,ipadx=75,ipady=75)
        button = Button(root, text="Quitter le jeu", command=root.destroy, font=(10), bg="#c94d4d")
        button.grid(row=3, column=1, columnspan=2, ipadx=100, ipady=40)
    def EcranDefaite(self):
        """Ecran de défaite à afficher"""
        for w in root.winfo_children():
            w.destroy()
            root.pack_propagate(0)
        root.title("Mastermind : Défaite")
        for i in range(4):
            root.rowconfigure(i,weight=1)
        for i in range(4):    
            root.columnconfigure(i,weight=1)
        label = Label(root, text="Pas de chance, vous n'avez pas trouvé la combinaison", font=(10))
        label.grid(row=0,column=0,columnspan=4)
        label = Label(root, text="Bonne combinaison :", font=(10))
        label.grid(row=1,column=0,columnspan=4)
        # Affichage combinaison user
        for i in range(4):
            valClr = CombinaisonATrouver[i]
            label = Label(root, text=valClr, bg=couleurs[valClr], relief=RAISED, font=(8))
            label.grid(row=2, column=i,ipadx=75,ipady=75)
        button = Button(root, text="Quitter le jeu", command=root.destroy, font=(10), bg="#c94d4d")
        button.grid(row=3, column=1, columnspan=2, ipadx=100, ipady=40)
        pass
# Texte d'explication (introduction)
root = Tk()
Affichage = Affichages()
Affichage.Intro() # Affichage texte d'introduction
# programme
Affichage.CombinaisonUser = [-1,-1,-1,-1]
# print(CombinaisonATrouver) # debug
couleurs = {-1:"grey","B":"white","N":"black"\
    ,0:"red",1:"yellow",2:"orange",3:"blue",4:"green",5:"white",6:"pink",7:"purple",8:"#00ffec"}
root = Tk()
root.geometry("600x600")
Affichage.Principale() # Affichage première fenêtre
root.mainloop() # Boucle d'affichage tkinter
