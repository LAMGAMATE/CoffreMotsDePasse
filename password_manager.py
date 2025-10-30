import json
import os

PASSWORD_FILE = "passwords.json"

def load_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

def save_passwords(passwords):
    with open(PASSWORD_FILE, "w") as f:
        json.dump(passwords, f)

def add_password():
    platform = input("Entrez le nom de la plateforme: ")
    password = input("Entrez le mot de passe: ")
    passwords = load_passwords()
    passwords[platform] = password
    save_passwords(passwords)
    print(f"Mot de passe pour {platform} sauvegarde")

def get_password():
    platform = input("Entrez le nom de la plateforme pour recuperer le mot de passe: ")
    passwords = load_passwords()
    if platform in passwords:
        print(f"Mot de passe pour {platform} est: {passwords[platform]}")
    else:
        print("Aucun mot de passe pour cette plateforme")

def main():
    while True:
        print("\nChoisissez une option:")
        print("1. Ajouter un mot de passe")
        print("2. Recuperer un mot de passe")
        print("3. Quitter")
        choice = input("Votre choix: ")
        if choice == "1":
            add_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            print("Au revoir!")
            break
        else:
            print("Choix incorrect, essayez encore")

if __name__ == "__main__":
    main()
