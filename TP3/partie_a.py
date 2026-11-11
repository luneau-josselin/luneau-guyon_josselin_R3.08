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
    class Utilisateur:
    def __init__(self, nom: str):
        self.nom = nom
        self.emprunts = []  # Liste d'objets Livre

    def emprunter_livre(self, livre: Livre) -> bool:
        if livre.emprunter(self.nom):
            self.emprunts.append(livre)
            return True
        return False

    def rendre_livre(self, livre: Livre) -> bool:
        if livre in self.emprunts and livre.rendre():
            self.emprunts.remove(livre)
            return True
        return False

    def afficher_emprunts(self):
        if not self.emprunts:
            print(f"{self.nom} n'a aucun livre en cours d'emprunt.")
        else:
            print(f"Livres empruntés par {self.nom} :")
            for livre in self.emprunts:
                print(f" - {livre.titre}")