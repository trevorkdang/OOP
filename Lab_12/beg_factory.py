from enemy_factory import EnemyFactory
from easy_troll import EasyTroll
from easy_goblin import EasyGoblin
from easy_ogre import EasyOgre
import random

class BeginnerFactory(EnemyFactory):
    
    """Represents an BeginnerFactory class"""

    def create_random_enemy(self):
        """Randomly chooses a integer and returns the Enemy class"""
        random_enemy = random.randint(1,3)
        if random_enemy == 1:
            return EasyTroll("Tiny Troll", random.randint(4,5))
        elif random_enemy == 2:
            return EasyOgre("Tiny Ogre", random.randint(3,5))
        else:
            return EasyGoblin("Tiny Goblin", random.randint(3,4))


if __name__ == "__main__":
    obj = BeginnerFactory()
    ret = obj.create_random_enemy()
    print(ret)
    
