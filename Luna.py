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

def injuryDeath():

	print('Your journey ends here. Experience again.')

def makeSpace():

	# Clears the terminal

	os.system('cls||clear')

def main():

	# Introductory text

	makeSpace()

	print('HackED 2020 - Luna\n')
	print('Developed in a 24-hour timeframe by Dylan and Taylor.\n')
	print('Luna is a program developed to help individuals reach')
	print('self-actualization through a series of events.\n')
	answer = input('Would you like to proceed? (Y/N) ')

	# Defining needed variables

	laptop = False # Player doesn't have the laptop
	hackedDoor = False # Player hasn't hacked the door
	rage = False # Player hasn't knocked down the pictures
	doorOpened = False # Player hasn't opened the bathroom door
	injury = False # Player doesn't have an injury
	gameState = 1 # Saves the progression of the game

	# Beginning the game

	makeSpace()

	while injury == False:

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
					makeSpace()
					print('The laptop is unlocked. It has Kali Linux installed on it.\n')
					laptop = True # The player now has the laptop
					gameState = gameState + 1 # The gameState is now at 2

					# Start of gameState two (escaping the room)

					answer = getPlayerInput(gameState)

					if answer == '1': # Player tries to opens the door
						makeSpace()
						print('The door has an electronic numpad. You don\'t know the code.\n')
						gameState = gameState + 98 # gameState is at 100
						answer = getPlayerInput(gameState)

						if answer == '1': # Hack the door
							makeSpace()
							hackedDoor = True
							print('You successfully hacked the door!')
							print('You open the door and look forward into a room filled with pictures.\n')
							gameState = gameState + 1 # gameState is at 101

							while rage == False:

								answer = getPlayerInput(gameState)

								if answer == '1':
									makeSpace()
									print('You walk up to the photos to get a good look at them.')
									print('All of the photos are of you.')

								if answer == '2':
									makeSpace()
									print('You frantically run around the room, knocking all of the pictures off the wall.')
									print('You reveal two doors.')
									rage = True
									gameState = gameState + 1 # gameState is at 102

									while doorOpened == False:

										answer = getPlayerInput(gameState)

										if answer == '1':
											makeSpace()
											print('As you open the door a bathroom is revealed.')
											print('The smell of bleach fills the air.')
											print('You spot a stall with an ajar door and a sink with a mirror above it.')
											doorOpened = True
											gameState = gameState + 1 # gameState is at 103
											answer = getPlayerInput(gameState)

											if answer == '1':
												makeSpace()
												print('The stall is empty graffiti on the wall and a dark red stain on the ceiling.')
												print('The graffiti reads "You stand in a croud of people. You are all the same."')

										if answer == '2':
											makeSpace()
											print('Opening the door reveals a cement wall.')
											print('The wall reads "I see you see me".\n')

						elif answer == '2': # Kick down the door
							makeSpace()
							print('You size up the door and approach it, kicking it full-force.')
							print('You failed to realize that the door is metal, and you broke your ankle.')
							print('The pain of your broken angle makes you faint.')
							print('While falling, you bash your head on the doorknob.\n')
							injuryDeath()
							injury = True
								
						else:
							makeSpace()

					elif answer == '2': # Player tries to open the window
						makeSpace()
						print('You can see outside. There is a security sensor on the edge of the window.')
						gameState = gameState + 1 # gameState is at 3
						answer = getPlayerInput(gameState)

						if answer == '1': #hack window
							makeSpace()
							print('You use the laptop to hack into the security sensor like a 1337 gamer.')
							print('The window opens. You appear to be on the 13th floor.')
							print('What do you do?')
							gameState = gameState + 1 #gameState at 4
							answer = getPlayerInput(gameState)

						elif answer == '2': #punch the window
							makeSpace()
							print('You square up with the window and throw hands.')
							print('The window counter attacks and breaks your Proximal Phalanges')
							injuryUpper = True
							print ('You should probably take a different approach.')
							answer = getPlayerInput(gameState)

				elif answer == '2': # Player tries to open the door
					makeSpace()
					print('The door has an electronic numpad. You don\'t know the code.\n')

				elif answer == '3': # Player tries to open the window
					makeSpace()
					print('You can see outside. There is a security sensor on the edge of the window.\n')

				else:
					makeSpace()

main()