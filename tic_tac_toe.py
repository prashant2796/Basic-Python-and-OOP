def display_board(board):
	"""
	This function is used to display 
	the board to the user.
	"""
	print('   |   |')
	print(' ' + board[7] +' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[4] +' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[1] +' | ' + board[2] + ' | ' + board[3])
	print('   |   |')

display_board(['#','X','O','X','O','X','O','X','O','X'])

def player_input():
	"""
	This function will get the user's choice
	of Either X or O
	OUTPUT = (Player 1 marker,Player 2 marker)
	"""
	marker = ''
	# Continue asking user until you get the valid input
	while not (marker == 'X' or marker == 'O'):
		marker = input("Player 1:Choose X or O: ").upper()
	# Set the marker according to the choice of first user
	if marker == 'X':
		return('X','O')
	else:
		return('O','X')
player_input()




