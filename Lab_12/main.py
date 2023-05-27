# Name: Co Chau and Trevor Dang
# Group: 8
# Date: 11/17/22
# Description: This is a program that allows the user to explore a dungeon and fight monsters along the way to escape.
from hero import Hero
from exp_factory import ExpertFactory
from beg_factory import BeginnerFactory
from map import Map
import check_input
import random

def main():
	
	"""This is the main function, that displays the hero's name, his HP, the
	map, and a menu that allows the player to move on the map. Loops multiple 
	times to determine what the player encounters in the maze. Then displays 
	congratulatory message when the game is finished."""

	map = Map()
	hero_name = input("What is your name, traveler? ")
	hero = Hero(hero_name, 50)
	dif = check_input.get_int_range("Difficulty:\n1.Beginner\n2.Expert\n", 1, 2)
	map_num = 1
	play_again = True

	while play_again:
		hero_loc = hero.loc
		print(hero)
		map.reveal(hero_loc)
		print(map.show_map(hero_loc))
		print("1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit")
		user_choice = check_input.get_int_range("Enter choice: ", 1, 5)
		if user_choice == 1:
			encounter = hero.go_north()
		elif user_choice == 2:
			encounter = hero.go_south()
		elif user_choice == 3:
			encounter = hero.go_east()
		elif user_choice == 4:
			encounter = hero.go_west()
		else:
			print("\nYou have failed to escape the maze!")
			play_again = False
		map.reveal(hero_loc)

		while encounter == "m":
			alive_monster = True
			if dif == 1:
				monster = BeginnerFactory().create_random_enemy()
			else:
				monster = ExpertFactory().create_random_enemy()
			print(f"You encounter a {monster}")
			while alive_monster:
				print(f"\n1. Attack {monster.name}\n2. Run Away")
				monster_menu = check_input.get_int_range("Enter choice: ", 1, 2)
				if monster_menu == 1:
					print(hero.attack(monster))
					if monster.hp > 0:
						print(monster.attack(hero))
					else:
						print(f"You have slain a {monster.name}\n")
						map.remove_at_loc(hero_loc)
						encounter = ""
						alive_monster = False
				else:
					print("You ran away...\n")
					direction = True
					while direction:
						rand = random.randint(1,4)
						if rand == 1 and hero_loc[0] > 0:
							encounter = hero.go_north()
							direction = False
						elif rand == 2 and hero_loc[0] < len(map)-1:
							encounter = hero.go_south()
							direction = False
						elif rand == 3 and hero_loc[1] < len(map[0])-1:
							encounter = hero.go_east()
							direction = False
						elif rand == 4 and hero_loc[1] > 0:
							encounter = hero.go_west()
							direction = False
					map.reveal(hero_loc)
					alive_monster = False
				
			

		if encounter == "x":
			print("You cannot go that way...\n")
		elif encounter == "n":
			print(f"There is nothing here...\n")
		elif encounter == "s":
			print(f"You wound up back at the start of the dungeon.\n")
		elif encounter == "i":
			hero.heal()
			map.remove_at_loc(hero_loc)
			print(f"You found a Health Potion!  You drink it to restore your health.\n")
		elif encounter == "f":
			print("Congratulations! You found the stairs to the next floor of the dungeon.")
			map_num += 1
			if map_num == 4:
				map_num = 1
			map.load_map(map_num)

main()