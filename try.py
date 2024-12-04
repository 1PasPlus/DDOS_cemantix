# Ouvrir le fichier des titres et traiter les mots
def extraire_mots_uniques(fichier_entree, fichier_sortie):
    mots_uniques = set()  # Utiliser un set pour stocker des mots uniques

    # Lire le fichier ligne par ligne
    with open(fichier_entree, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            # Supprimer les espaces ou sauts de ligne inutiles
            ligne = ligne.strip()
            # Remplacer les underscores (_) par des espaces pour isoler les mots
            mots = ligne.replace("_", " ").split()
            # Ajouter les mots au set
            mots_uniques.update(mots)

    # Écrire les mots uniques dans le fichier de sortie
    with open(fichier_sortie, 'w', encoding='utf-8') as fichier:
        for mot in sorted(mots_uniques):  # Trier les mots par ordre alphabétique
            fichier.write(mot + '\n')

# Chemin du fichier frwiki et du fichier de sortie
fichier_entree = 'famille.txt'
fichier_sortie = 'family.txt'

# Appeler la fonction pour générer le fichier de mots uniques
extraire_mots_uniques(fichier_entree, fichier_sortie)
