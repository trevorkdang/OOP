from enemy_factory import EnemyFactory
from troll import Troll
from ogre import Ogre
from goblin import Goblin
import random

class ExpertFactory(EnemyFactory):
    """Represents a ExpertFactory class"""

    def create_random_enemy(self):
        """Randomly chooses a integer and returns the Enemy class"""
        random_enemy = random.randint(1,3)
        if random_enemy == 1:
            return Troll("Tremedous Troll", random.randint(10,14))
        elif random_enemy == 2:
            return Ogre("Lumbering Ogre", random.randint(8,12))
        else:
            return Goblin("Vicious Goblin", random.randint(6,10))


if __name__ == "__main__":
    obj = ExpertFactory()
    ret = obj.create_random_enemy()
    print(ret.name)
    
