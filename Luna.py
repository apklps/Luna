import os, time

def open_file():

	name = 'options_' + str(game_state)
	print(name)
	return file = open(name, 'r')

def close_file():

	file.close()

def print_options(options):

	i = 1

	for line in options:
		print(i, line, end = '')
		i = i + 1
	print('\n')

def remove_options(option):

	

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

	laptop = False # Player doensn't have the laptop
	game_state = 0 # Saves the progression of the game

	# Beginning the game

	os.system('cls||clear')

	if answer == 'Y':
		print('You wake up in a dimly lit room.')
		print('You see a door on the opposite wall of you.')
		print('You see a laptop on a shelf on the left wall.')
		print('You see a window on the right wall.\n')

		print('What do you do?\n')
		open_file()
		print_options(options_one)

		answer = input('Option: ')

		if answer == '1':
			os.system('cls||clear')
			print('The laptop is unlocked. It has Kali Linux installed on it.\n')
			laptop = True # The player now has the laptop
			game_state = game_state + 1 # The game_state is now at 1

		elif answer == '2':
			os.system('cls||clear')
			print('The door has an electronic numpad. You don\'t know the code.\n')
			remove_options(answer)
		elif answer == '3':
			os.system('cls||clear')
			print('You can see outside. There is a security sensor on the edge of the window.\n')
			print('What do you do?')
			print('1) Grab the laptop.')
			print('2) Try to open the door.')

main()