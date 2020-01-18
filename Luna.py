import os, time

def open_file(game_state):

	# Opens option file depending on the player's game state

	name = 'options_' + str(game_state) + '.txt'
	file = open(name, 'r')
	return file

def print_options(file):

	# Prints out the options in the text file

	i = 1

	for line in file:
		print(str(i) + line, end = '')
		i = i + 1
	print('\n')

def main():

	# Clears the terminal

	os.system('cls||clear')

	# Introductory text

	print('HackED 2020 - Luna\n')
	print('Developed in a 24-hour timeframe by Dylan and Taylor.\n')
	print('Luna is a program developed to help individuals reach')
	print('self-actualization through a series of events.\n')
	answer = input('Would you like to proceed? (Y/N) ')

	# Defining needed variables

	laptop = False # Player doesn't have the laptop
	injury = False # Player doesn't have an injury
	game_state = 1 # Saves the progression of the game

	# Beginning the game

	os.system('cls||clear')

	# Game State One (No laptop, first room)

	if answer == 'Y':
		print('You wake up in a dimly lit room.')
		print('You see a door on the opposite wall of you.')
		print('You see a laptop on a shelf on the left wall.')
		print('You see a window on the right wall.\n')

		# Loops options until the player grabs the laptop

		while laptop == False:

			print('What do you do?\n')
			file = open_file(game_state)
			print_options(file)

			answer = input('Option: ')

			if answer == '1':
				os.system('cls||clear')
				print('The laptop is unlocked. It has Kali Linux installed on it.\n')
				laptop = True # The player now has the laptop
				game_state = game_state + 1 # The game_state is now at 2

			elif answer == '2':
				os.system('cls||clear')
				print('The door has an electronic numpad. You don\'t know the code.\n')

			elif answer == '3':
				os.system('cls||clear')
				print('You can see outside. There is a security sensor on the edge of the window.\n')

main()