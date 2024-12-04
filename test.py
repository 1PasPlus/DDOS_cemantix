import random
import csv
import pandas as pd

# Charger les données du fichier Lexique383.tsv
df = pd.read_csv('lexique\Lexique383.tsv', sep='\t')

# Extraire les mots et leurs fréquences
word_frequencies = dict(zip(df['ortho'], df['freqlivres']))

# Liste des mots fréquents à mettre en priorité
frequent_words = [
    "le", "la", "les", "de", "un", "une", "des", "et", "à", "il", "elle", "en", "pour", "avec", "par", "que", "qui", "sur", "dans", "ne", "pas", "ce", "se", "son", "sa", "ses", "au", "du", "ou", "y", "mais", "nous", "vous", "ils", "elles", "être", "avoir", "faire", "comme", "plus", "si", "tout", "bien", "peut", "sont", "était", "cela", "cet", "cette", "aussi", "leur", "lui", "dont", "ainsi", "entre", "elle-même", "eux", "cela", "celui", "celui-ci", "cela", "chacun", "avant", "après", "depuis", "lorsque", "ainsi", "autre", "cependant", "peu", "encore", "chaque", "grand", "petit", "tout", "autant", "même", "très", "tel", "pendant", "temps", "homme", "femme", "ville", "pays", "France", "monde", "histoire", "guerre", "roi", "famille", "groupe", "article", "travail", "eau", "feu", "terre", "air", "personne", "année", "jour", "vie", "moi", "toi", "nous", "vous",
    "amour", "époque", "gouvernement", "république", "empire", "roi", "reine", "président", "élection", "démocratie", "capitale", "continent", "pouvoir", "autorité", "loi", "militaire", "armée", "religion", "église", "culture", "science", "technologie", "santé", "éducation", "université", "école", "langue", "littérature", "art", "musée", "musique", "peinture", "architecture", "philosophie", "économie", "finance", "commerce", "industrie", "banque", "province", "région", "Europe", "Asie", "Afrique", "Amérique", "Océanie"
]

# Charger l'ancienne liste des mots français
with open('liste_francais_optimise.txt', 'r', encoding='utf-8') as f:
    original_words = [line.strip() for line in f]

# Enlever les mots fréquents déjà présents dans la liste originelle pour éviter les doublons
remaining_words = [word for word in original_words if word not in frequent_words]

# Trier les mots restants par fréquence d'apparition, du plus fréquent au moins fréquent
remaining_words.sort(key=lambda x: word_frequencies.get(x, 0), reverse=True)

# Créer la nouvelle liste des mots en mettant les mots fréquents en priorité
new_word_list = frequent_words + remaining_words

# Sauvegarder la nouvelle liste dans le fichier
with open('liste_francais_optimise_frequence.txt', 'w', encoding='utf-8') as f:
    for word in new_word_list:
        f.write(f"{word}\n")

print("La liste de mots a été réorganisée selon la fréquence d'apparition pour améliorer l'efficacité de la recherche.")
