from character import Character

class Magician(Character):
    def cast_spell(self, target):
        if self.weapon:
            print(f"{self.name} casts a spell on {target.name}")
            self.attack(target)
        else:
            print(f"{self.name} has no weapon to cast a spell.")