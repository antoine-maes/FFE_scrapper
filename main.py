import time
from send_mail import envoyer_mail
from scrapper import check_competition

url = input("Entrez l'URL de la page web cible: ")

email_envoye = False

while not email_envoye:
    if check_competition(url):
        email_envoye = envoyer_mail(
            subject="FFE - Inscription au concours",
            body="L'inscription au concours est ouverte"
        )
    else:
        print("L'inscription n'est pas encore ouverte. Réessayer dans une heure.")
        time.sleep(3600)  # Attendre une heure (3600 secondes) avant de réessayer