import random
print("Welcome to TIC TAC TOE!")


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


def place_marker(board,marker,position):
	"""
	This function will place marker 
	on a specified postion by the user.
	"""
	board[position] = marker


def win_check(board,mark):
	"""
	The function takes in the board and 
	the marker and checks to see if that
	marker has won.

	WIN TICTACTOE?
	Check if any row or column or any diagonal
	has the same marker.
	"""
	return ((board[7] ==  board[8] ==  board[9] == mark) or # across the top
    (board[4] ==  board[5] ==  board[6] == mark) or # across the middle
    (board[1] ==  board[2] ==  board[3] == mark) or # across the bottom
    (board[7] ==  board[4] ==  board[1] == mark) or # down the left side
    (board[8] ==  board[5] ==  board[2] == mark) or # down the middle
    (board[9] ==  board[6] ==  board[3] == mark) or # down the right side
    (board[7] ==  board[5] ==  board[3] == mark) or # diagonal
    (board[9] ==  board[5] ==  board[1] == mark)) # diagonal


def choose_first():
	"""
	This function ramdomly decides which player 
	will play first.
	It makes use of the ramdom.randint() module 
	to randomly select any number
	"""
	flip = random.randint(0,1)

	if flip == 0:
		return 'Player 1'
	else:
		return 'Player 2'


def space_check(board,position):
	"""
	This function returns boolean indicating whether the 
	space on the board is freely available.
	"""
	return board[position] == ' '


def full_board_check(board):
	"""
	This function checks whether the board is full or not
	and returns a boolean value.
	"""
	for i in range(1,10):
		if space_check(board,i):
			return False
	#  We return True Board is full if
	return True


def player_choice(board):
	"""
	This function asks for a player's next position(as 1-9 numbers)
	and then uses the space_check function to check if it's the free
	position.If it is, return the position for later use.
	"""
	position = 0

	while position not in range(1,10) or not space_check(board,position):
		position = int(input("choose a position: (1-9) "))

	return position

def replay():
	"""
	This function asks the player if they want to play again and return 
	a boolean True if they want to play again
	"""
	choice = input("Play Again? Enter Yes or No ").upper()
	return choice == 'YES'


def tictactoe_game():
	"""
	This function runs all the other functions
	for the actual game play.
	"""

	# While loop to keep running the game.
	while True:
		# Set up the board and the marker
		game_board = [' ']*10
		player1_marker,player2_marker = player_input()

		# Choose which User will go first
		turn = choose_first()
		print(turn + 'will go first')
	    
		play_game = input("Ready to play Tic Tac Toe? y or n ").lower()

		if play_game == 'y':
			game_on = True
		else:
			game_on = False

		while game_on:

			if turn == 'Player 1':
				# Show the Board
				display_board(game_board)

				# Choose a position
				position = player_choice(game_board)

				# Place the marker on the position
				place_marker(game_board,player1_marker,position)

				# Check if they won
				if win_check(game_board,player1_marker):
					display_board(game_board)
					print("Player 1 has Won!!")
					game_on = False
				else:
					# Check whether there is a Tie
					if full_board_check(game_board):
						display_board(game_board)
						print("The Game is a tie!!")
						game_on = False
					else:
						# If not return the turn to player 2
						turn = 'Player 2'

			else:
				# Show the Board
				display_board(game_board)

				# Choose a position
				position = player_choice(game_board)

				# Place the marker on the position
				place_marker(game_board,player2_marker,position)

				# Check if they won
				if win_check(game_board,player2_marker):
					display_board(game_board)
					print("Player 2 has Won!!")
					game_on = False
				else:
					# Check whether there is a Tie
					if full_board_check(game_board):
						display_board(game_board)
						print("The Game is a tie!!")
						game_on = False
					else:
						# If not return the turn to player 1
						turn = 'Player 1'
	    		
		if not replay():
			break

tictactoe_game()