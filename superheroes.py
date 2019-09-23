import random

class Ability:
    def __init__(self, name, max_damage):
       self.name = name
       self.max_damage = max_damage

    def attack(self):
        return random.randint(0, self.max_damage)
       # TODO: Instantiate the variables listed in the docstring with then
       # values passed in
class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)
        # TODO: Create instance variables for the values passed in.

class Hero:
    def __init__(self, name, current_health, starting_health=100):
      self.name = name
      self.starting_health = starting_health
      self.abilities = []
      self.armors = []
      self.current_health = current_health
       # TODO: Initialize instance variables values as instance variables
       # (Some of these values are passed in above,
       # others will need to be set at a starting value)
       # abilities and armors are lists that will contain objects that we can use

    def add_ability(self, ability):
        self.abilities.append(ability)


    def attack(self):
        total_damage = 0
        for i in self.abilities:
            total_damage += i.attack()
        return total_damage


    def add_armor(self, armor):
        self.armors.append(armor)


    def defend(self):
        total_defense = 0
        for hero in self.armors:
            total_defense += hero.block()
        return total_defense


    def take_damage(self, damage):
        self.current_health -= damage

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            # print('{} is dead'.format(self.name))
            return False

    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            hero_attack = self.attack()
            opponent_attack = opponent.attack()
            self.take_damage(opponent_attack)
            opponent.take_damage(hero_attack)
        if self.is_alive() == False and opponent.is_alive == False:
            print('Draw! Both heroes went unconscious from their injuries!')
        elif self.is_alive() == False:
            print(f'{opponent.name} won the Great Fantasy War')
        elif opponent.is_alive() == False:
            print(f'{self.name} won the Great Fantasy War')




if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    Rimuru = Hero("Rimuru", 1000)
    Itachi = Hero("Itachi", 1000)
    ability1 = Ability("Sharigan", 330)
    ability2 = Ability("Slicing Water Cut", 240)
    ability3 = Ability("Amertartsu", 320)
    ability4 = Ability("Genjustsu", 230)
    Rimuru.add_ability(ability1)
    Rimuru.add_ability(ability2)
    Itachi.add_ability(ability3)
    Itachi.add_ability(ability4)
    Rimuru.fight(Itachi)
