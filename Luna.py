import os, time

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

	playing = True

	# Beginning the game

	os.system('cls||clear')

	if answer == 'Y':
		print('You wake up in a dimly lit room.')
		print('You see a door on the opposite wall of you.')
		print('You see a laptop on a shelf on the left wall.')
		print('You see a window on the right wall.\n')

		print('What do you do?')
		print('1) Open the laptop.')
		print('2) Look out the window.')
		print('3) Try to open the door.\n')

		answer = input('Option: ')

		if answer == '1':
			os.system('cls||clear')
			print('\nThe laptop is unlocked. It has Kali Linux installed on it.\n')
			print('What do you do?')
			print('1) Try to open the window.')
			print('2) Try to open the door.')
		elif answer == '2':
			print('\nYou can see outside. There is a security sensor on the edge of the window.')
		elif answer == '3':
			print('\nThe door is locked.')


main()