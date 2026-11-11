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

            # Demande du coup jusqu'à ce qu'il soit valide
            valide = False
            while not valide:
                x, y = joueur_actuel.prochain_coup(self.grille)
                valide = self.grille.jouer(x, y, joueur_actuel.symbole)

            # Vérification de la victoire
            if self.grille.est_gagnant(joueur_actuel.symbole):
                if affichage:
                    self.grille.afficher()
                    print(f" Victoire du joueur {joueur_actuel.symbole} ! ")
                return joueur_actuel.symbole

            self.tour += 1

        if affichage:
            self.grille.afficher()
            print("Match nul !")
        return "NUL"