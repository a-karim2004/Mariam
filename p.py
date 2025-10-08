from termcolor import colored
import time


def happy_birthday_zara():
    """Affiche un message d'anniversaire pour Zara avec des couleurs."""

    messages = [
        "🎉 Joyeux Anniversaire, Ramash ! 🎉",
        "🎂 Que cette journée soit remplie de bonheur, de joie et d'amour ! 🎈",
        "🎁 Tous nos vœux pour une année incroyable ! ✨"
    ]

    colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

    # Effet de démarrage
    print(colored("\n" + "*" * 50, "yellow"))
    print(colored("***** Fêtons l'anniversaire de Zara !  *****", "yellow"))
    print(colored("*" * 50 + "\n", "yellow"))

    # Affichage du message principal avec un effet d'écriture
    for message in messages:
        for char in message:
            print(colored(char, choice(colors)), end="", flush=True)
            time.sleep(0.05)  # Pause pour l'effet
        print()  # Nouvelle ligne
        time.sleep(1)  # Pause entre les messages

    print(colored("\n" + "-" * 50, "cyan"))
    print(colored("© Créé avec amour l'infini∞.", "cyan"))
    print(colored("-" * 50 + "\n", "cyan"))


# Utilisation de random.choice pour les couleurs
# Utilisation de random.choice pour les couleurs
from random import choice

# Exécuter la fonction
happy_birthday_zara()