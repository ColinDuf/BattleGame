# main.py
from gears.weapon import Weapon
from gears.armor import Armor
from arena import Arena
from characters.barbarian import Barbarian
from characters.wizard import Wizard, Spell
import random
from colorama import Fore, Style, init

# Initialise colorama
init(autoreset=True)

def main():

    def choose_opponent():
        character_choices = ["Bot Barbare", "Bot Magicien"]
        random_choice = random.choice(character_choices)

        if random_choice == "Bot Barbare":
            return Barbarian(name="Bot Barbare", hp=100, weapon=Weapon(name="Hache", damage=15), armor=Armor(name="Bouclier", protection=10), isPlayer1=False)
        elif random_choice == "Bot Magicien":
            return Wizard(name="Bot Magicien", hp=80, mana=100, weapon=Weapon(name="Dague", damage=15), armor=Armor(name="Cape magique", protection=5), isPlayer1=False, spells=[Spell(name="Boule de feu", damage=35, mana_cost=15)])

    while True:
        # Utilisateur choisit un personnage en entrant "1" pour Barbare ou "2" pour Magicien
        player_choice = input(Fore.BLUE +"Choisissez votre personnage (1 pour Barbare / 2 pour Magicien): ")
        if player_choice == "1":
            player_character = Barbarian(name="Barbare", hp=100, weapon=Weapon(name="Hache", damage=15), armor=Armor(name="Bouclier", protection=10), isPlayer1=True)
        elif player_choice == "2":
            player_character = Wizard(name="Magicien", hp=80, mana=100, weapon=Weapon(name="Dague", damage=15), armor=Armor(name="Cape magique", protection=5), isPlayer1=True, spells=[Spell(name="Boule de feu", damage=20, mana_cost=15),Spell(name="Télépathie", damage=40, mana_cost=50)])
        else:
            print(Fore.RED + "Choix invalide. Veuillez choisir entre 1 et 2." + Style.RESET_ALL)
            continue

        # Créez une instance d'Arena avec le joueur et un adversaire aléatoire
        arena = Arena(player_character, choose_opponent())

        # Appelez la méthode fight de l'Arena pour gérer le combat
        arena.fight()

        # Demandez au joueur s'il veut recommencer le jeu après la défaite
        restart_game = input("Voulez-vous recommencer le jeu? (Oui/Non): ").lower()
        if restart_game != 'oui':
            print("Merci d'avoir joué. Au revoir!")
            break

if __name__ == "__main__":
    main()
