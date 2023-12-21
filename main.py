
from gears.weapon import Weapon
from gears.armor import Armor
from characters.character import Character

Axe = Weapon('Axe', '5')
Sword = Weapon('Sword', '10')

Leather = Armor('Leather', '25')
Stone = Armor('Stone', '50')


# Instancier les personnages
john = Character("John", 100)
jane = Character("Jane", 100)

# John attaque Jane avec une épée
john.attack(jane, Sword)

# Jane attaque John avec une hache
jane.attack(john, Axe)

