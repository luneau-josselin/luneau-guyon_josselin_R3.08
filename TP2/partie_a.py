class Grille:
    def __init__(self):
        # Initialisation d'une grille 3x3 avec des espaces vides
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def afficher(self):
        """Affiche la grille de manière lisible dans le terminal."""
        print("\n  0   1   2")
        for i, row in enumerate(self.grid):
            print(f"{i} " + " | ".join(row))
            if i < 2:
                print("  " + "---+" * 2 + "---")
        print()