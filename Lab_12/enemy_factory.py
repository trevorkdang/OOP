import abc

class EnemyFactory(abc.ABC):
    """Represents a EnemyFactory class"""
    @abc.abstractclassmethod
    def create_random_enemy(self):
        pass