from puppystate import PuppyState

class StateAsleep(PuppyState):
    
    def plays(self, puppy):
        return "The puppy is asleep. It doesn't want to play right now"

    def feeds(self, puppy):
        return "The puppy wakes up and comes running to eat"

if __name__ == "__main__":
    sleep = StateAsleep()
    print(sleep.feeds(sleep))