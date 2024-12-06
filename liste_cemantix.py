import random
import csv
import pandas as pd

# Charger les données du fichier Lexique383.tsv
df = pd.read_csv('lexique\Lexique383.tsv', sep='\t')

# Filtrer les mots pour n'inclure que ceux qui sont des verbes à l'infinitif, noms communs, adverbes, ou adjectifs
filtered_df = df[(df['cgram'] == 'VER') & (df['lemme'] == df['ortho']) | (df['cgram'].isin(['NOM', 'ADV', 'ADJ']))]
filtered_words_set = set(filtered_df['ortho'])

# Charger l'ancienne liste des mots français
with open('liste_francais.txt', 'r', encoding='utf-8') as f:
    original_words = [line.strip() for line in f]

# Pré-calculer un dictionnaire des fréquences pour réduire le nombre d'opérations
frequency_dict = dict(zip(df['ortho'], df['freqlivres']))

# Filtrer les mots pour enlever les verbes conjugués, en ne gardant que les formes à l'infinitif, noms communs, adverbes, et adjectifs
filtered_words = [word for word in original_words if word in filtered_words_set]

# Trier les mots restants par fréquence d'apparition, du plus fréquent au moins fréquent
filtered_words.sort(key=lambda x: frequency_dict.get(x, 0), reverse=True)

# Sauvegarder la nouvelle liste dans le fichier
with open('liste_francais_optimise_cemantix.txt', 'w', encoding='utf-8') as f:
    f.writelines(f"{word}\n" for word in filtered_words)

print("La liste de mots a été réorganisée pour n'inclure que des verbes à l'infinitif, noms communs, adverbes, et adjectifs, et améliorer l'efficacité de la recherche.")
