import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os 
from dotenv import load_dotenv

load_dotenv()

def envoyer_mail(subject, body):
    password = os.environ.get('PASSWORD')
    sender_email = os.environ.get('FROM')
    receiver_email = os.environ.get('TO')
    login = sender_email

    smtp_server="smtp.gmail.com"
    port=587
    
    try:
        # Créer l'objet de message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Ajouter le corps du message
        msg.attach(MIMEText(body, 'plain'))

        # Se connecter au serveur SMTP
        print("Connexion au serveur SMTP...")
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(login, password)

        # Envoyer l'email
        print("Envoi de l'email...")
        server.sendmail(sender_email, receiver_email, msg.as_string())

        print("Email envoyé avec succès")
        server.quit()

        return True
        
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email: {e}")
        server.quit()
        return False

    

