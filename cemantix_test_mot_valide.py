from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Charger la liste des mots français depuis le fichier
with open('liste_francais.txt', 'r', encoding='utf-8') as f:
    mots = [line.strip() for line in f]

random.shuffle(mots)

# Configurer le WebDriver (assurez-vous que le chromedriver est dans votre PATH)
driver = webdriver.Chrome()

# Ouvrir l'URL
driver.get('https://cemantix.certitudes.org')

# Attendre que la page se charge complètement
time.sleep(2)

# Ouvrir le fichier pour écrire les mots valides
with open('mots_valides.txt', 'w', encoding='utf-8') as fichier_valide:
    # Boucle pour envoyer chaque mot
    for mot in mots:
        try:
            # Trouver le champ de saisie
            champ_saisie = driver.find_element(By.ID, 'cemantix-guess')

            # Effacer le champ de saisie
            champ_saisie.clear()

            # Entrer le mot
            champ_saisie.send_keys(mot)

            # Cliquer sur le bouton 'Envoyer'
            bouton_envoyer = driver.find_element(By.ID, 'cemantix-guess-btn')
            bouton_envoyer.click()

            # Attendre un court instant pour que la réponse soit affichée
            #time.sleep(0.5)

            # Vérifier si le champ d'erreur est vide (mot valide)
            champ_erreur = driver.find_element(By.ID, 'cemantix-error')
            if champ_erreur.text.strip() == "":
                # Si aucune erreur trouvée, le mot est valide
                print(f"Mot valide : {mot}")
                fichier_valide.write(mot + '\n')
                fichier_valide.flush()  # Forcer l'écriture immédiate dans le fichier
            else:
                print(f"Mot non valide : {mot}")

        except Exception as e:
            print(f"Une erreur est survenue avec le mot '{mot}': {e}")
            continue

# Fermer le navigateur
driver.quit()
