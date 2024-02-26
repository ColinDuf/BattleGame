from .character import Character
import random
from colorama import Fore, init

init(autoreset=True)

class Spell:
    def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

class Wizard(Character):
    def __init__(self, name, hp, mana, weapon, armor, isPlayer1, spells):
        super().__init__(name, hp, weapon, armor, isPlayer1)
        self.spells = spells
        self.mana = mana

    def attack(self, target,isPlayer=False):
        if isPlayer:
            weaponChoosen = False
            while (not weaponChoosen):
                print(Fore.YELLOW + "\nIl vous reste " +str(self.mana)+ " de mana, choisissez un sort :" + Fore.RESET)
                print("1 - "+self.weapon.name)
                for i in range(len(self.spells)):
                    print(str(i+2)+" - "+self.spells[i].name)
                try:
                    weapon = int(input())
                except ValueError:
                    print(Fore.RED + "Merci de sélectionner un chiffre entre 1 et " + str(len(self.spells) + 1) + "\n" + Fore.RESET)
                    continue
                if (weapon>0 and weapon<=(len(self.spells)+1)):
                    weaponChoosen = True
                    break
                else:
                    print(Fore.RED + "Merci de sélectionner un chiffre entre 1 et " + str(len(self.spells) + 1) + "\n" + Fore.RESET)
        else:
            weapon = random.randint(1,len(self.spells)+1)
        if (weapon > 1):
            if (self.spells[weapon-2].mana_cost <= self.mana):
                damages = (self.spells[weapon-2].damage)
                self.mana -= self.spells[weapon-2].mana_cost
                target.hp -= damages
                print(Fore.MAGENTA + self.name + " inflige " + str(damages) + " dégâts ! il reste " + str(target.hp) + " HP à " + target.name + Fore.RESET)


            else:
                if(self.isPlayer1):
                    print(Fore.YELLOW + (self.name) + " n'a pas assez de mana pour faire cette attaque")
                damages = (self.weapon.damage - target.armor.protection)
                if (damages < 0):
                    damages = 0
                target.hp -= damages    
                print (Fore.MAGENTA + self.name + " inflige " + str(damages) + " dégâts ! il reste "+ str(target.hp) + " HP à " + target.name)

        else:
            damages = (self.weapon.damage - target.armor.protection)
            if (damages < 0):
                damages = 0
            target.hp -= damages
            print (Fore.MAGENTA +self.name + " inflige " + str(damages) + " dégâts ! il reste "+ str(target.hp) + " HP à " + target.name)

    