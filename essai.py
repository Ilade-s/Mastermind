def essai():
    """Demande à l'utilisateur et renvoie une liste des quatres couleurs choisies (de 0 à 8) si inputs valides (sinon -1 en cas d'erreur)
    
    Paramètres
    ----------
    Aucun paramètre d'entrée

    Sortie
    -------
    list[int]
        liste contenant la combinaison entrée par l'utilisateur
    """
    clrs = input("Couleurs choisies au format xxxx (ex : 0123) entre 0 et 8 inclus : ")
    CombClrs = []
    for i in clrs:
        try:
            CombClrs.append(int(i))
        except ValueError:
            return(-1)
    return(CombClrs)

if __name__ == "__main__": # test
    combinaison = essai()
    if combinaison==-1:
        print("Combinaison invalide")
    else:
        print(combinaison)