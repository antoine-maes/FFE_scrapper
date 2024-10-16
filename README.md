# FFE Scrapper

Ce projet est un scrapper pour vérifier l'ouverture des inscriptions à un concours sur un site web spécifique et envoyer un email de notification lorsque l'inscription est ouverte.

## Prérequis

-   Python 3.x

## Installation

1. Installez les dépendances :

    ```sh
    pip install -r requirements.txt
    ```

2. Configurez les variables d'environnement en créant un fichier `.env` à la racine du projet avec le contenu suivant :

    ```env
    PASSWORD="votre_mot_de_passe"
    FROM="votre_email@gmail.com"
    TO="email_destinataire@example.com,autre_email_destinataire@example.com"
    ```

## Utilisation

1. Exécutez le script principal :

    ```sh
    python main.py
    ```

2. Entrez l'URL de la page web cible lorsque vous y êtes invité.

Le script vérifiera périodiquement si l'inscription est ouverte et enverra un email de notification lorsque c'est le cas.

## Fichiers

-   `main.py` : Le script principal qui lance le scrapper et envoie les emails.
-   `scrapper.py` : Contient la fonction `check_competition` qui vérifie l'état des inscriptions.
-   `send_mail.py` : Contient la fonction `envoyer_mail` qui envoie les emails de notification.
-   `requirements.txt` : Liste des dépendances Python nécessaires pour le projet.
-   `.env` : Fichier de configuration pour les variables d'environnement (non inclus dans le dépôt Git).

## Auteur

Antoine Maes

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
