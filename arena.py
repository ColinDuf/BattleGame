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
                current_character.attack(self.second_character, isPlayer=True)
            else:
                current_character.attack(self.second_character, isPlayer=False)

            if self.second_character.hp <= 0:
                print(f"{Fore.CYAN}Partie terminé {self.second_character.name} a été vaincu!{Fore.RESET}")
                break
            else:
                print(f"{self.second_character.name} a survécu !\n")

            current_character, self.second_character = self.second_character, current_character