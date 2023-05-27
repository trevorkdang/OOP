import check_input
from puppy import Puppy
from stateasleep import StateAsleep
from stateeat import StateEat
from stateplay import StatePlay

def main():
    print("Congratulations on your new puppy!\nWhat would you like to do?")
    play_again = True
    pup = Puppy()
    
    while play_again:
        act = check_input.get_int_range("1. Feed the puppy \n2. Play with the puppy \n3. Quit \nEnter choice: ", 1, 3)
        if act == 1 and pup.feeds == 0 and pup.plays == 0:
            print(pup.give_food())
            pup.change_state(StateEat())
            pup.inc_feeds()

        elif act == 1 and pup.feeds == 1 and pup.plays == 0:
            print(pup.give_food())
            pup.inc_feeds()

        elif act == 1 and pup.feeds == 2 and pup.plays == 0:
            print(pup.give_food())
            print("The puppy ate so much it fell asleep!")
            pup.change_state(StateAsleep())
            pup.reset()

        elif act == 2 and pup.feeds == 0 and pup.plays == 0:
            print(pup.throw_ball())
                
        elif act == 2 and pup.feeds == 1 and pup.plays == 0:
            print(pup.throw_ball())
            pup.reset()
            pup.change_state(StatePlay())
            pup.inc_plays()

        elif act == 2 and pup.feeds == 0 and pup.plays == 1:
            print(pup.throw_ball())
            pup.inc_plays()

        elif act == 2 and pup.feeds == 0 and pup.plays == 2:
            print(pup.throw_ball())
            print("The puppy played so much it fell asleep!")
            pup.change_state(StateAsleep())
            pup.reset()

        else:
            play_again = False
        








if __name__ == "__main__":
    main()