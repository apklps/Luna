import os, time, sys, random

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

	# Prints player options and gets what option they want

	print('What do you do?\n')
	file = openFile(gameState)
	printOptions(file)
	answer = input('Option: ')
	return answer

def surrealDeath():

	# Surreal death text

	print('You don\'t exist. Experience again soon.\n')

def injuryDeath():

	# Normal death text

	print('YOU ARE DEAD. Experience again soon.\n')

def makeSpace():

	# Clears the terminal

	os.system('cls||clear')

def falseOption():

	# What the game prints when an invalid option is used

	print('\nThat was not an option.')
	surrealDeath()
	sys.exit()

def doorOptions(answer, gameState, rage, doorOpened, mirrorPeer):

	if answer == '1': # Hack the door
		makeSpace()
		hackedDoor = True
		print('You successfully hacked the door!')
		print('You open the door and look forward into a room filled with pictures.\n')
		gameState = gameState + 1 # gameState is at 101

		while rage == False:
			rage = pictureOptions(answer, gameState, rage, doorOpened, mirrorPeer)

	elif answer == '2': # Kick down the door
		makeSpace()
		print('You size up the door and approach it, kicking it full-force.')
		print('You failed to realize that the door is metal, and you broke your ankle.')
		print('The pain of your broken angle makes you faint.')
		print('While falling, you bash your head on the doorknob.\n')
		surrealDeath()
		injury = True
		return injury

	else:
		falseOption()

def pictureOptions(answer, gameState, rage, doorOpened, mirrorPeer):

	answer = getPlayerInput(gameState)

	if answer == '1':
		makeSpace()
		print('You walk up to the photos to get a good look at them.')
		print('All of the photos are of you.')

	elif answer == '2':
		makeSpace()
		print('You frantically run around the room, knocking all of the pictures off the wall.')
		print('You reveal two doors.')
		rage = True
		gameState = gameState + 1 # gameState is at 102

		while doorOpened == False:
			answer = getPlayerInput(gameState)
			doorOpened = pictureDoorOptions(answer, gameState, mirrorPeer)

	else:
		falseOption()

	return rage

def pictureDoorOptions(answer, gameState, mirrorPeer):

	if answer == '1':
		makeSpace()
		print('As you open the door a bathroom is revealed.')
		print('The smell of bleach fills the air.')
		print('You spot a stall with an ajar door and a sink with a mirror above it.')
		doorOpened = True
		gameState = gameState + 1 # gameState is at 103
		answer = getPlayerInput(gameState)

		while mirrorPeer == False:
			bathroomOptions(answer, gameState)

		return doorOpened

	elif answer == '2':
		makeSpace()
		print('Opening the door reveals a cement wall.')
		print('The wall reads "I see you see me".\n')
		doorOpened = False
		return doorOpened

	else:
		falseOption()

def bathroomOptions(answer, gameState):

	if answer == '1':
		makeSpace()
		print('The stall is empty graffiti on the wall and a dark red stain on the ceiling.')
		print('The graffiti reads "You stand in a croud of people. You are all the same."')

	elif answer == '2':
		makeSpace()
		print('You walk up to the mirror and wipe it off with your hand.')
		print('You look in the mirror, but your reflection doesn\'t make eye contact.')
		print('What did you do?\n')
		time.sleep(3)
		gameState = gameState + 1 # gameState is at 104
		answer = getPlayerInput(gameState)

	else:
		falseOption()

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
	mirrorPeer = False # Player hasn't looked in the mirror
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

						injury = doorOptions(answer, gameState, rage, doorOpened, mirrorPeer)

					elif answer == '2': # Player tries to open the window
						makeSpace()
						print('You can see outside. There is a security sensor on the edge of the window.')
						gameState = gameState + 1 # gameState is at 3
						answer = getPlayerInput(gameState)

						if answer == '1': #hack window
							makeSpace()
							print('You use the laptop to hack into the security sensor like a 1337 gamer.')
							print('The window opens. You appear to be on the 13th floor.')
							
							gameState = gameState + 1 #gameState at 4
							answer = getPlayerInput(gameState)
							if answer == '1': #jump thru
								makeSpace()
								print('Being a total badass was always your identity; you jump through')
								print('the window without any concern for your well being.\n')
								time.sleep(3)
								makeSpace()
								print('You land safely in a dumpster filled with inflated bags of laughing gas.')
								print('Some of the gas is released, and you giggle.')
								print('As you pull yourself out, you see that you are in a back alley.\n')
								print('SUDDENLY, a vicious dog confronts you, snarling, foaming at the mouth.')
								gameState = gameState + 1
								answer - getPlayerInput(gameState)
								

							elif answer == '2': #Turn back
								makeSpace()
								print('As you turn back you hear the roar of an airplane getting closer.')
								print('Your entire world explodes as it crashes into the window, shattering')
								print('your self-esteem.')
								injuryDeath()
						elif answer == '2': #punch the window
							makeSpace()
							print('You square up with the window and throw hands.')
							print('The window counter attacks and breaks your Proximal Phalanges')
							print('You hear the voice of your deceased taekwondo master:\n')
							print('"You absolute bafoon. You bring shame to our lineage."')
							injuryDeath()

					else:
						falseOption()

				elif answer == '2': # Player tries to open the door
					makeSpace()
					print('The door has an electronic numpad. You don\'t know the code.\n')

				elif answer == '3': # Player tries to open the window
					makeSpace()
					print('You can see outside. There is a security sensor on the edge of the window.\n')

				else:
					makeSpace()

main()