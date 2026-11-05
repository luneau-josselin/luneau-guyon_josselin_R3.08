import random

class Joueur:
    def __init__(self, symbole):
        self.symbole = symbole

    def prochain_coup(self, grille):
        raise NotImplementedError("La méthode prochain_coup doit être réimplémentée.")