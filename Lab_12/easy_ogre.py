from entity import Entity
import random
class EasyOgre(Entity):

    """Represents a EasyOgre class.
    Attributes:
    name (str): name of the entity
    max_hp (int): max health point of the entity
    hp (int): current health point of the entity
    """

    def __init__(self, name, max_hp):
        """Initializes the name, max_hp, and hp"""
        super().__init__(name, max_hp)
        self._hp = self._max_hp

    def attack(self, entity):
        """Calculates and displays the damage taken when attacking"""
        damage = random.randint(1,4)
        entity.take_damage(damage)
        return "{} attacks {} for {} damage.".format(self.name, entity.name, damage)
