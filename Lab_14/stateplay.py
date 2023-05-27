from puppystate import PuppyState

class StatePlay(PuppyState):
    
    def plays(self, puppy):
        return "You throw the ball again and the puppy excitedly chases it."

    def feeds(self, puppy):
        return "The puppy is too busy playing with the ball to eat right now. "