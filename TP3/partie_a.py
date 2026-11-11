class Livre:
    def __init__(self, titre: str, auteur: str, annee: int, disponible: bool = True, emprunteur: str = None):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = disponible
        self.emprunteur = emprunteur

    def afficher(self):
        statut = "Disponible" if self.disponible else f"Emprunté par {self.emprunteur}"
        print(f"'{self.titre}' par {self.auteur} ({self.annee}) - {statut}")

    def emprunter(self, nom_utilisateur: str) -> bool:
        if self.disponible:
            self.disponible = False
            self.emprunteur = nom_utilisateur
            return True
        return False

    def rendre(self) -> bool:
        if not self.disponible:
            self.disponible = True
            self.emprunteur = None
            return True
        return False