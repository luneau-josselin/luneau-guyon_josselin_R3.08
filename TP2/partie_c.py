class JeuMorpion:
    def __init__(self, j1, j2):
        self.grille = Grille()
        self.joueurs = [j1, j2]
        self.tour = 0

    def jouer_partie(self, affichage=True):
        """Exécute une partie complète entre les deux joueurs."""
        while not self.grille.est_plein():
            joueur_actuel = self.joueurs[self.tour % 2]
            
            if affichage:
                self.grille.afficher()
                print(f"Tour du joueur {joueur_actuel.symbole}")