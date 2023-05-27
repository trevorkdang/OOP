from puppystate import PuppyState

class StateEat(PuppyState):
    
    def plays(self, puppy):
        return "The puppy looks up from its food and chases the ball you threw."

    def feeds(self, puppy):
        return "The puppy continues to eat as you add another scoop of kibble to its bowl."