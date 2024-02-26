from colorama import Fore

class Character():
    def __init__(self, name, hp, weapon, armor, isPlayer1):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armor = armor
        self.isPlayer1 = isPlayer1

    def attack(self, target, isPlayer=False):  # Ajoutez isPlayer=False comme argument
        damages = (self.weapon.damage - target.armor.protection)

        if damages < 0:
            damages = 0
        target.hp -= damages

        return Fore.GREEN + f"{self.name} inflige {damages} dégâts ! Il reste {target.hp} HP à {target.name}" + Fore.RESET
