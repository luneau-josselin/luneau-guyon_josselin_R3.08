import os
import sys

# Importation des fonctions d'appui de la Partie C
from partie_c import charger_liste_mots, choisir_mot, construire_masque, nettoyer_texte

# 🎨 Dessin ASCII du pendu selon le nombre d'erreurs (0 à 7)
ASCII_PENDU = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """
]

FICHIER_SCORES = "scores.txt"

# ------------------------------------------------------------------------------
# GESTION DU HALL OF FAME (SCORES)
# ------------------------------------------------------------------------------
def charger_scores(fichier: str = FICHIER_SCORES) -> dict[str, float]:
    """Charge le dictionnaire nom -> victoires depuis scores.txt."""
    scores = {}
    if not os.path.exists(fichier):
        return scores
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            for ligne in f:
                ligne = ligne.strip()
                if ":" in ligne:
                    nom, val = ligne.split(":", 1)
                    try:
                        scores[nom.strip()] = float(val.strip())
                    except ValueError:
                        continue
    except IOError:
        pass
    return scores

def sauvegarder_scores(scores: dict[str, float], fichier: str = FICHIER_SCORES) -> None:
    """Enregistre le dictionnaire de scores dans scores.txt."""
    try:
        with open(fichier, "w", encoding="utf-8") as f:
            for nom, victoires in scores.items():
                f.write(f"{nom}:{victoires}\n")
    except IOError as e:
        print(f"Erreur lors de la sauvegarde des scores : {e}")

# ------------------------------------------------------------------------------
# BOUCLE DU JEU DU PENDU
# ------------------------------------------------------------------------------
def jouer_pendu(mot_secret: str) -> bool:
    """
    Exécute une partie de Pendu.
    Renvoie True en cas de victoire, False en cas de défaite.
    """
    masque = construire_masque(mot_secret)
    erreurs = 0
    max_erreurs = 7
    lettres_proposees = set()

    while erreurs < max_erreurs and "_" in masque:
        # Affichage du pendu et de l'état actuel
        index_ascii = min(erreurs, len(ASCII_PENDU) - 1)
        print(ASCII_PENDU[index_ascii])
        print(f"Mot : {' '.join(masque)}")
        print(f"Erreurs : {erreurs}/{max_erreurs} | Lettres proposées : {', '.join(sorted(lettres_proposees))}")

        # Saisie du joueur
        saisie = input("Entrez une lettre : ").strip()
        if not saisie:
            continue

        # Nettoyage de la lettre (majuscule et sans accent)
        lettre = nettoyer_texte(saisie[0])

        # Vérification si la lettre a déjà été proposée
        if lettre in lettres_proposees:
            print(f"\n⚠️ La lettre '{lettre}' a déjà été proposée. Aucun décompte d'erreur.")
            continue

        lettres_proposees.add(lettre)

        # Traitement de la lettre
        if lettre in mot_secret:
            print(f"\n✅ Bien joué ! La lettre '{lettre}' est dans le mot.")
            for idx, char in enumerate(mot_secret):
                if char == lettre:
                    masque[idx] = lettre
        else:
            print(f"\n❌ Raté ! La lettre '{lettre}' n'est pas dans le mot.")
            erreurs += 1

    # Condition de fin de partie
    if "_" not in masque:
        print(f"\n🎉 Gagné ! Le mot était bien : {mot_secret}")
        return True
    else:
        print(ASCII_PENDU[-1])
        print(f"\n☠️ Perdu, le mot était {mot_secret}")
        return False

# ------------------------------------------------------------------------------
# MENU PRINCIPAL & REJOUABILITÉ
# ------------------------------------------------------------------------------
def main():
    scores = charger_scores()
    print("=================================")
    print("        JEU DU PENDU             ")
    print("=================================")

    joueur = input("Entrez votre nom : ").strip() or "Joueur"
    if joueur in scores:
        print(f"Bon retour {joueur} ! Victoires actuelles : {scores[joueur]}")
    else:
        scores[joueur] = 0.0

    while True:
        print("\n--- MENU ---")
        print("1. Mode Solo (Mot aléatoire)")
        print("2. Mode 2 Joueurs / Tournoi (Proposer un mot pour son voisin)")
        print("3. Voir les scores (Hall of Fame)")
        print("4. Quitter")

        choix = input("Votre choix (1-4) : ").strip()

        if choix == "1":
            banque = charger_liste_mots(["PYTHON", "ÉLÉPHANT", "ALGORITHME", "PROGRAMMATION"])
            mot_secret = choisir_mot(banque)
            victoire = jouer_pendu(mot_secret)
            if victoire:
                scores[joueur] = scores.get(joueur, 0.0) + 1.0

        elif choix == "2":
            mot_saisi = input("Joueur 1, entrez le mot secret pour votre voisin : ").strip()
            # Masquer la saisie en faisant défiler l'écran
            print("\n" * 50)
            mot_secret = nettoyer_texte(mot_saisi)
            if not mot_secret:
                print("Mot invalide.")
                continue
            
            victoire = jouer_pendu(mot_secret)
            if victoire:
                scores[joueur] = scores.get(joueur, 0.0) + 1.0

        elif choix == "3":
            print("\n=== HALL OF FAME ===")
            if not scores:
                print("Aucun score enregistré.")
            else:
                for nom, victoires in scores.items():
                    print(f"- {nom} : {victoires} victoire(s)")

        elif choix == "4":
            sauvegarder_scores(scores)
            print("Scores enregistrés dans scores.txt. À bientôt !")
            break
        else:
            print("Choix invalide.")

        # Rejouabilité
        if choix in ["1", "2"]:
            rejouer = input("\nVoulez-vous faire une autre partie ? (o/n) : ").strip().lower()
            if rejouer != 'o':
                sauvegarder_scores(scores)
                print("Scores enregistrés dans scores.txt. Merci d'avoir joué !")
                break

if __name__ == "__main__":
    main()