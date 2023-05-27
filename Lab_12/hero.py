from entity import Entity
from map import Map
import random

class Hero(Entity):
    """Represents a hero class
    Attributes:
    name (str): name of the entity
    max_hp (int): max health point of the entity
    hp (int): current health point of the entity
    loc (tuple): the coordinates of the entity
    """

    def __init__(self, name, max_hp):
        """Initializes the name, max hp, and location of the hero"""
        super().__init__(name, max_hp)
        self._loc = [0,0]

    def attack(self, entity):
        """Calculates and displays the damage taken when attacking"""
        damage = random.randint(2,5)
        entity.take_damage(damage)
        return "{} attacks {} for {} damage.".format(self.name, entity.name, damage)
    
    @property
    def loc(self):
        """Access the location of the player"""
        return self._loc

    def go_north(self):
        """Returns the location of the player after going up on the map"""
        if self._loc[0] > 0:
            self._loc[0] -= 1
            return Map()[self._loc[0]][self._loc[1]]
        return 'x'

    def go_south(self):
        """Returns the location of the player after going down on the map"""
        if self._loc[0] < len(Map())-1:
            self._loc[0] += 1
            return Map()[self._loc[0]][self._loc[1]]
        return 'x'

    def go_west(self):
        """Returns the location of the player after going left on the map"""
        if self._loc[1] > 0:
            self._loc[1] -= 1
            return Map()[self._loc[0]][self._loc[1]]
        return 'x'

    def go_east(self):
        """Returns the location of the player after going right on the map"""
        if self._loc[1] < len(Map()[0])-1:
            self._loc[1] += 1
            return Map()[self._loc[0]][self._loc[1]]
        return 'x'
 

if __name__ == "__main__":
    human = Hero("King", 50)
    print(human.go_east())

