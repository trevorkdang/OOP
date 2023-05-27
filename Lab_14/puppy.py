from stateasleep import StateAsleep
from stateeat import StateEat
from stateplay import StatePlay

class Puppy:
    def __init__(self):
        self._state = StateAsleep()
        self._feeds = 0
        self._plays = 0

    @property
    def feeds(self):
        return self._feeds
    
    @property 
    def plays(self):
        return self._plays

    def change_state(self, new_state):
        self._state = new_state
    
    def throw_ball(self):
        return self._state.plays(self)

    def give_food(self):
        return self._state.feeds(self)

    def inc_plays(self):
        self._plays += 1
    
    def inc_feeds(self):
        self._feeds += 1

    def reset(self):
        self._plays = 0
        self._feeds = 0

if __name__ == "__main__":
    pup = Puppy()
    print(pup.throw_ball())
    print(pup.give_food())
    print(pup.feeds)
    