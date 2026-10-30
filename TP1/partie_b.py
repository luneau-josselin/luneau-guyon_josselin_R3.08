import random

def jouer_partie(borne_min: int = 1, borne_max: int = 100, max_essais: int = 10) -> bool:
    """Gère une partie du jeu 'Devine le nombre'."""
    # Étape 1 : Génération du nombre secret
    nombre_secret = random.randint(borne_min, borne_max)
    print(f"\n--- Devine le nombre entre {borne_min} et {borne_max} ---")
    print(f"Vous avez {max_essais} essais maximum !")

    # Boucle des essais
    for essai in range(1, max_essais + 1):
        # Saisie sécurisée
        while True:
            try:
                saisie = int(input(f"\nEssai {essai}/{max_essais} - Votre proposition : "))
                break
            except ValueError:
                print("⚠️ Veuillez entrer un nombre entier valide !")

        # Étape 3 & 4 : Comparaison
        if saisie < nombre_secret:
            print("« Trop petit »")
        elif saisie > nombre_secret:
            print("« Trop grand »")
        else:
            print(f"🎉 « Gagné » en {essai} essai(s) !")
            return True

    # Fin des 10 essais sans succès
    print(f"\n☠️ Perdu ! Vous avez dépassé les {max_essais} essais.")
    print(f"Le nombre secret était : {nombre_secret}")
    return False

def devine_le_nombre():
    """Fonction principale avec bornes et rejouabilité (Bonus)."""
    print("=================================")
    print("   JEU : DEVINE LE NOMBRE        ")
    print("=================================")

    # Bornes personnalisées
    try:
        saisie_min = input("Borne minimale (défaut = 1) : ").strip()
        b_min = int(saisie_min) if saisie_min else 1

        saisie_max = input("Borne maximale (défaut = 100) : ").strip()
        b_max = int(saisie_max) if saisie_max else 100

        if b_min >= b_max:
            print("Borne min invalide. Utilisation des bornes par défaut 1 - 100.")
            b_min, b_max = 1, 100
    except ValueError:
        print("Saisie invalide. Utilisation des bornes par défaut 1 - 100.")
        b_min, b_max = 1, 100

    # Rejouabilité
    while True:
        jouer_partie(borne_min=b_min, borne_max=b_max)
        rejouer = input("\nVoulez-vous rejouer ? (o/n) : ").strip().lower()
        if rejouer != 'o':
            print("Merci d'avoir joué !")
            break


if __name__ == "__main__":
    devine_le_nombre()