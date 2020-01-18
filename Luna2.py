import os, time

def openFile(gameState):

	# Opens option file depending on the player's game state

	name = 'options_' + str(gameState) + '.txt'
	file = open(name, 'r')
	return file

def printOptions(file):

	# Prints out the options in the text file

	i = 1

	for line in file:
		print(str(i) + line, end = '')
		i = i + 1
	print('\n')

def getPlayerInput(gameState):

	print('What do you do?\n')
	file = openFile(gameState)
	printOptions(file)
	answer = input('Option: ')
	return answer

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
	injuryUpper = False # Player doesn't have an upper-body injury
	injuryLower = False # Player doesn't have an upper-body injury
	gameState = 1 # Saves the progression of the game
	gameEnd = False

	# Beginning the game

	os.system('cls||clear')

	while injuryUpper == False or injuryLower == False:

		# Game State One (No laptop, first room)

		if answer == 'Y':
			print('You wake up in a dimly lit room.')
			print('You see a door on the opposite wall of you.')
			print('You see a laptop on a shelf on the left wall.')
			print('You see a window on the right wall.\n')

			# Loops options until the player grabs the laptop

			while laptop == False:

				answer = getPlayerInput(gameState)

				if answer == '1': # Player grabs the laptop
					os.system('cls||clear')
					print('The laptop is unlocked. It has Kali Linux installed on it.\n')
					laptop = True # The player now has the laptop
					gameState = gameState + 1 # The gameState is now at 2

					# Start of gameState two (escaping the room)

					answer = getPlayerInput(gameState)

					if answer == '1': # Player tries to opens the door
						os.system('cls||clear')
						print('The door has an electronic numpad. You don\'t know the code.\n')
						gameState = gameState + 98 # gameState is at 100
						answer = getPlayerInput(gameState)

						if answer == '1': # Hack the door
							os.system('cls||clear')
							print('You successfully hacked the door!')


					elif answer == '2': # Player tries to open the window
						os.system('cls||clear')
						print('You can see outside. There is a security sensor on the edge of the window.\n')
						gameState = gameState + 1 # gameState is at 3
						answer = getPlayerInput(gameState)
						if answer == '1': #hack window
							os.system('cls||clear')
							print('You use the laptop to hack into the security sensor like a 1337 gamer.\n')
							print('The window opens. You appear to be on the 13th floor.\n')
							print('What do you do?')

				elif answer == '2': # Player tries to open the door
					os.system('cls||clear')
					print('The door has an electronic numpad. You don\'t know the code.\n')

				elif answer == '3': # Player tries to open the window
					os.system('cls||clear')
					print('You can see outside. There is a security sensor on the edge of the window.\n')

main()