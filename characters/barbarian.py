# barbarian.py
from .character import Character
from colorama import Fore

class Barbarian(Character):
    def __init__(self, name, hp, weapon, armor, isPlayer1):
        super().__init__(name, hp, weapon, armor, isPlayer1)

    def attack(self, target, isPlayer=False):
        print(super().attack(target, isPlayer))
        print(Fore.GREEN + "Coup critique! " + super().attack(target)+Fore.GREEN+" suplémentaire !" + Fore.RESET)
        
