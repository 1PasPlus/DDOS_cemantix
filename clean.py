import re

def nettoyer_fichier(fichier_entree, fichier_sortie):
    # Expression régulière pour matcher uniquement les mots contenant des lettres (accents inclus)
    regex = re.compile(r'^[A-Za-zÀ]+$')

    with open(fichier_entree, 'r', encoding='utf-8') as fichier:
        mots_valides = [ligne.strip() for ligne in fichier if regex.match(ligne.strip())]

    # Écrire les mots nettoyés dans un nouveau fichier
    with open(fichier_sortie, 'w', encoding='utf-8') as fichier:
        for mot in mots_valides:
            fichier.write(mot + '\n')

# Chemins des fichiers
fichier_entree = 'mots_uniques.txt'  # Le fichier à nettoyer
fichier_sortie = 'mots_nettoyes.txt'  # Le fichier de sortie

# Appeler la fonction pour nettoyer le fichier
nettoyer_fichier(fichier_entree, fichier_sortie)
