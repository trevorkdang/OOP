import abc
class Entity(abc.ABC):
    
    """Represent a Entity class.
    Attribute:
    name (str): name of the entity
    max_hp (int): max health point of the entity
    hp (int): current health point of the entity
    """

    def __init__(self, name, max_hp):
        """Initializes the name, max_hp, and hp of the entity"""
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp

    @property
    def name(self):
        """Access the name of the entity"""
        return self._name
    
    @property
    def hp(self):
        """Access the hp of the entity"""
        return self._hp

    def take_damage(self, dmg):
        """Subtract the damage from the entity hp"""
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0
    
    def heal(self):
        self._hp = self._max_hp

    def __str__(self):
        """Display the entity's name and hp"""
        return "{}\nHP: {}/{}".format(self._name, self._hp, self._max_hp)

    @abc.abstractclassmethod
    def attack(self, entity):
        pass

if __name__ == "__main__":
    h = Entity("kitt", 50)
    print(h)