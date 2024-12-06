from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Charger la liste des mots français depuis le fichier
with open('liste_francais_optimise_frequence.txt', 'r', encoding='utf-8') as f:
    mots = [line.strip() for line in f]

# Configurer le WebDriver (assurez-vous que le chromedriver est dans votre PATH)
driver = webdriver.Chrome()

# Ouvrir l'URL
driver.get('https://cemantix.certitudes.org')

# Attendre que la page se charge complètement
time.sleep(2)

# Boucle pour envoyer chaque mot
for mot in mots:
    try:
        # Trouver le champ de saisie
        champ_saisie = driver.find_element(By.ID, 'pedantix-guess')

        # Effacer le champ de saisie
        champ_saisie.clear()

        # Entrer le mot
        champ_saisie.send_keys(mot)

        # Appuyer sur Entrée pour valider
        champ_saisie.send_keys(Keys.RETURN)

        # Attendre un court instant avant le prochain mot
        #time.sleep(0.01)

    except Exception as e:
        print(f"Une erreur est survenue avec le mot '{mot}': {e}")
        continue

# Fermer le navigateur
#driver.quit()
