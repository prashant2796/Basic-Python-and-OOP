test_board = ['#','X','O','X','O','X','O','X','O','X']
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

# display_board(['#','X','O','X','O','X','O','X','O','X'])

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
# player_input()

def place_marker(board,marker,position):
	"""
	This function will place marker 
	on a specified postion by the user.
	"""
	board[position] = marker
# place_marker(test_board,'&',6)

def win_check(board,marker):
	"""
	The function takes in the board and 
	the marker and checks to see if that
	marker has won.

	WIN TICTACTOE?
	Check if any row or column or any diagonal
	has the same marker.
	"""
	for i in board[1:10]:
		# Check to see if there is consecutive marker in a row.If Yes,return True
		if board[i] == marker and board[i+1] == marker and board[i+2] == marker:

			return True
		# Check to see if there is consecutive marker in a column.If Yes,return True
		elif board[i] == marker and board[i+3] == marker and board[i+6] == marker:

			return True
		# Check to see if there is consecutive marker in a diagonal.If Yes,return True
		elif board[i] == marker and board[i+4] == marker and board[i+8] == marker:
			return True
		else:
			return False


















