import random
import unicodedata

def nettoyer_texte(mot: str) -> str:
    """
    Nettoie le mot : supprime les accents et convertit en majuscules.
    Permet de gérer sereinement les mots comme 'ÉLÉPHANT' -> 'ELEPHANT'.
    """
    mot_nfkd = unicodedata.normalize('NFKD', mot)
    mot_sans_accent = "".join([c for c in mot_nfkd if not unicodedata.combining(c)])
    return mot_sans_accent.upper()

def charger_liste_mots(fichier_ou_liste) -> list[str]:
    """
    1. Charger une liste de mots depuis une liste Python ou un fichier.txt.
    """
    if isinstance(fichier_ou_liste, list):
        return fichier_ou_liste
    
    try:
        with open(fichier_ou_liste, "r", encoding="utf-8") as f:
            mots = [ligne.strip() for ligne in f if ligne.strip()]
            return mots if mots else ["PYTHON", "DEVELOPPEUR", "ALGORITHME"]
    except IOError:
        print(f"Fichier '{fichier_ou_liste}' introuvable. Utilisation d'une liste par défaut.")
        return ["PYTHON", "DEVELOPPEUR", "ALGORITHME"]

def choisir_mot(liste: list[str]) -> str:
    """
    2. choisir_mot(liste) renvoie un mot au hasard en MAJUSCULES.
    """
    if not liste:
        return "PYTHON"
    mot_selectionne = random.choice(liste)
    return nettoyer_texte(mot_selectionne)

def construire_masque(mot: str) -> list[str]:
    """
    3. Construire un masque : liste de '_' de même longueur que le mot.
    """
    return ["_"] * len(mot)


# ==============================================================================
# JEU D'ESSAI ET TESTS
# ==============================================================================
if __name__ == "__main__":
    # Liste de test
    mots_test = ["python", "elephant", "programmation"]
    
    # 1. Chargement
    liste = charger_liste_mots(mots_test)
    
    # 2. Choix du mot
    mot = choisir_mot(liste)
    print(f"Mot choisi : {mot}")
    
    # 3. Construction du masque
    masque = construire_masque(mot)
    print(f"masque (\"{mot}\") -> {masque}")