from map import Map
from rooms import Room 
from player import Player

def check_win():
	return False

def print_room(current_room):
	print(current_room.get_id())

def print_player_options(current_room, player):
	print("This is where the players options he can choose will be printed")

def normalise_input(player_action):
	input_list = player_action.split(" ")
	
	return input_list

def execute_action(game_map, player, player_action):
	if player_action[0] == "go":
		player.current_room = player.current_room.get_exit(player_action[1])


def main():
	print("-" * 100)
	print("Welcome to the game!!!!")

	game_map = Map()
	entrance = Room()
	entrance.set_id("en")
	entrance.set_x(2)
	entrance.set_y(2)
	game_map.map_matrix[entrance.get_y()][entrance.get_x()] = entrance
	game_map.rooms_in_map.append(entrance)

	game_map.init_gen_map()
	game_map.display_map()

	player_name = input("Please enter your name: ")
	player = Player(player_name, entrance)



	while True:
		if check_win():
			print("You Win! wooohoo!!")
			break

		print_room(player.current_room)

		print_player_options(player.current_room, player)

		player_action = input("You choose to: ")
		
		'''
		We need a normalise function here to handle the players input (possibly put in another file like in 
		the thing we made in our independant projects) but for now its created in this game.py file and only
		splits the players input by spaces
		'''
		player_action = normalise_input(player_action)

		execute_action(game_map, player, player_action)


if __name__ == "__main__":
    main()