import random

# Liste des mots fréquents à mettre en priorité
frequent_words = [
    "le", "la", "les", "de", "un", "une", "des", "et", "à", "il", "elle", "en", "pour", "avec", "par", "que", "qui", "sur", "dans", "ne", "pas", "ce", "se", "son", "sa", "ses", "au", "du", "ou", "y", "mais", "nous", "vous", "ils", "elles", "être", "avoir", "faire", "comme", "plus", "si", "tout", "bien", "peut", "sont", "était", "cela", "cet", "cette", "aussi", "leur", "lui", "dont", "ainsi", "entre", "elle-même", "eux", "cela", "celui", "celui-ci", "cela", "chacun", "avant", "après", "depuis", "lorsque", "ainsi", "autre", "cependant", "peu", "encore", "chaque", "grand", "petit", "tout", "autant", "même", "très", "tel", "pendant", "temps", "homme", "femme", "ville", "pays", "France", "monde", "histoire", "guerre", "roi", "famille", "groupe", "article", "travail", "eau", "feu", "terre", "air", "personne", "année", "jour", "vie", "moi", "toi", "nous", "vous",
    "amour", "époque", "gouvernement", "république", "empire", "roi", "reine", "président", "élection", "démocratie", "capitale", "continent", "pouvoir", "autorité", "loi", "militaire", "armée", "religion", "église", "culture", "science", "technologie", "santé", "éducation", "université", "école", "langue", "littérature", "art", "musée", "musique", "peinture", "architecture", "philosophie", "économie", "finance", "commerce", "industrie", "banque", "province", "région", "Europe", "Asie", "Afrique", "Amérique", "Océanie", "Angleterre", "Allemagne", "Italie", "Espagne", "Belgique", "Suisse", "Russie", "Chine", "Japon", "Inde", "Australie", "Canada", "États-Unis", "Mexique", "Brésil", "Argentine", "Égypte", "Maroc", "Tunisie", "Algérie", "Nigeria", "Kenya", "Afrique du Sud", "Arabie Saoudite", "Iran", "Irak", "Israël", "Palestine", "Turquie", "Grèce", "Portugal", "Suède", "Norvège", "Finlande", "Danemark", "Pays-Bas", "Autriche", "Hongrie", "Pologne", "Tchéquie", "Slovaquie", "Roumanie", "Bulgarie", "Serbie", "Croatie", "Slovénie", "Bosnie", "Ukraine", "Biélorussie", "Lituanie", "Lettonie", "Estonie", "Géorgie", "Arménie", "Azerbaïdjan", "Kazakhstan", "Mongolie", "Thaïlande", "Vietnam", "Indonésie", "Malaisie", "Philippines", "Corée", "Singapour", "Nouvelle-Zélande", "Islande", "Cuba", "Chili", "Venezuela", "Pérou", "Colombie", "Bolivie", "Uruguay", "Paraguay", "Guyane", "Suriname", "Honduras", "Guatemala", "Nicaragua", "Costa Rica", "Panama", "Haïti", "Jamaïque", "Bahamas", "Barbade", "Saint-Domingue", "République Dominicaine", "Port-au-Prince", "Caracas", "Buenos Aires", "Brasília", "Santiago", "Lima", "Bogota", "Montréal", "Toronto", "Ottawa", "Vancouver", "Washington", "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "San Francisco", "Seattle", "Miami", "Las Vegas", "Boston", "Philadelphie", "Detroit", "Dallas", "Atlanta", "Monaco", "Vatican", "Lisbonne", "Madrid", "Rome", "Paris", "Bruxelles", "Amsterdam", "Vienne", "Berlin", "Londres", "Dublin", "Edimbourg", "Glasgow", "Moscou", "Saint-Pétersbourg", "Stockholm", "Oslo", "Helsinki", "Copenhague", "Varsovie", "Prague", "Budapest", "Sofia", "Bucarest", "Belgrade", "Zagreb", "Ljubljana", "Sarajevo", "Tirana", "Skopje", "Athènes", "Nicosie", "Istanbul", "Ankara", "Damas", "Beyrouth", "Jérusalem", "Tel Aviv", "Amman", "Riyad", "Téhéran", "Bagdad", "Kaboul", "Islamabad", "New Delhi", "Katmandou", "Dhaka", "Yangon", "Bangkok", "Hanoï", "Vientiane", "Phnom Penh", "Kuala Lumpur", "Singapour", "Jakarta", "Bandar Seri Begawan", "Dili", "Manille", "Séoul", "Tokyo", "Pékin", "Ulaanbaatar", "Hanoï", "Canberra", "Wellington"
]

# Charger l'ancienne liste des mots français
with open('liste_francais_optimise.txt', 'r', encoding='utf-8') as f:
    original_words = [line.strip() for line in f]

# Enlever les mots fréquents déjà présents dans la liste originelle pour éviter les doublons
remaining_words = [word for word in original_words if word not in frequent_words]

# Mélanger la liste des mots restants pour un ordre aléatoire
random.shuffle(remaining_words)

# Créer la nouvelle liste des mots en mettant les mots fréquents en priorité
new_word_list = frequent_words + remaining_words

# Sauvegarder la nouvelle liste dans le fichier
with open('liste_francais_optimise.txt', 'w', encoding='utf-8') as f:
    for word in new_word_list:
        f.write(f"{word}\n")

print("La liste de mots a été réorganisée pour améliorer l'efficacité de la recherche.")
