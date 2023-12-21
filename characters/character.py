class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        

def attack(self, target,weapon):
        if self.weapon:
            damage = self.weapon.damage
            target.receive_damage(damage)

def receive_damage(self, damage):
        if self.armor:
            damage -= self.armor.defense
        self.hp -= max(0, damage)
        if self.hp <= 0:
            print(f"{self.name} has been defeated!")