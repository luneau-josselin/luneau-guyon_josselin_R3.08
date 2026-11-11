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


def simuler_parties(nb_parties=20):
    """Simule nb_parties automatisées entre deux IA (Partie C)."""
    scores = {"X": 0, "O": 0, "NUL": 0}
    for i in range(nb_parties):
        j1 = JoueurIA("X")
        j2 = JoueurIA("O")
        jeu = JeuMorpion(j1, j2)
        resultat = jeu.jouer_partie(affichage=False)
        scores[resultat] += 1
    
    print(f"--- Résultats sur {nb_parties} parties IA vs IA ---")
    print(f"Victoires X : {scores['X']}")
    print(f"Victoires O : {scores['O']}")
    print(f"Matchs nuls : {scores['NUL']}")


# Script principal de démonstration
if __name__ == "__main__":
    print("=== TEST PARTIE A : Jeu d'essai de la Grille ===")
    g = Grille()
    g.jouer(0, 0, "X")
    g.jouer(0, 1, "O")
    g.jouer(1, 1, "X")
    g.afficher()
    g.jouer(0, 0, "O")  # Refusé (occupée)
    g.jouer(3, 0, "O")  # Refusé (hors grille)
    print("X est gagnant ?", g.est_gagnant("X"))
    g.jouer(2, 2, "X")
    print("X est gagnant après (2,2) ?", g.est_gagnant("X"))

    print("\n=== TEST PARTIE C : IA vs IA (20 parties) ===")
    simuler_parties(20)

    print("\n=== LANCEMENT D'UNE PARTIE HUMAIN VS IA MALIN ===")
    humain = JoueurHumain("X")
    ia_maligne = JoueurIAMalin("O")
    partie = JeuMorpion(humain, ia_maligne)
    partie.jouer_partie()