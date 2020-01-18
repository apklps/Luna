import os, time

def main():

	# Clears the terminal

	os.system('cls||clear')

	# Introductory text

	print('HackED 2020 - Luna\n')
	print('Developed in a 24-hour timeframe by Dylan and Taylor.\n')
	print('Luna is a program developed to help individuals reach')
	print('self-actualization through a series of questions.\n')
	answer = input('Would you like to proceed? (Y/N) ')

	# Defining needed variables

	talking = True

	# Beginning the conversation

	os.system('cls||clear')

	if answer == 'Y':
		print('If you would like to quit at any time, just type "quit".\n')
		print('The conversation will start in five seconds.')
		time.sleep(5)
		os.system('cls||clear')

		# Initial Conversation

		print('Hello, my name is Luna.')
		name = input('What\'s your name?\n\n' + 'My name is: ')

		print('\nHello %s' % name)

		while talking:
			pass
			
			


main()