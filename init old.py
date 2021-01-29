import random
#init crée une liste de 4 couleurs a découvrir 
def init() -> list[int]:
    """Crée une liste de 4 valeurs aléatoires entre 0 et 8

    Paramètres
    ----------
    Aucun paramètre d'entrée

    Sortie
    -------
    list[int]
        liste de valeurs aléatoire entre 0 et 8 inclus
    """
    couleur = random.sample(range(8), 4)
    return(couleur)

if __name__ == "__main__":
    combinaison = init()
    print(combinaison)