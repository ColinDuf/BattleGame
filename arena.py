from colorama import Fore

class Arena:
    def __init__(self, first_character, second_character):
        self.first_character = first_character
        self.second_character = second_character

    def fight(self):
        current_character = self.first_character
        print(f"\nVous affrontez maintenant un {self.second_character.name}!")

        while True:
            if current_character.isPlayer1:
                # Si c'est au tour du joueur, laissez-le choisir l'attaque
                current_character.attack(self.second_character, isPlayer=True)
            else:
                # Si c'est au tour du bot, laissez-le attaquer automatiquement
                current_character.attack(self.second_character, isPlayer=False)

            # Vérifiez si l'adversaire est vaincu
            if self.second_character.hp <= 0:
                print(f"{Fore.CYAN}Partie terminé {self.second_character.name} a été vaincu!{Fore.RESET}")
                break
            else:
                print(f"{self.second_character.name} a survécu !\n")

            # Changez le personnage attaquant
            current_character, self.second_character = self.second_character, current_character