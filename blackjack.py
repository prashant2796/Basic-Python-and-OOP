import random

suits = ('Hearts' , 'Diamonds' , 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five' , 'Six', 'Seven', 
	     'Eight', 'Nine' , 'Ten', 'Jack', 'Queen', 'King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
		  'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card():
	"""
	This Class Basically describes the card with 
	two attributes suits and rank.
	"""
	def __init__(self,suits,ranks):
		self.suits = suits
		self.ranks = ranks

	def __str__(self):
		return (f"{self.ranks} of {self.suits}")


class Deck():
	"""
	This class describes a pack of 52 unique cards as 
	a list.
	"""

	def __init__(self):
		# Initializing an empty list that will content all the cards
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def __str__(self):
		deck_comp = ''
		for card in self.deck:
			deck_comp += '\n' + card.__str__()
		return "The Deck has: "+ deck_comp

	def shuffle(self):
		"""
		This Function will shuffle the pack of cards
		""" 
		random.shuffle(self.deck)

	def deal(self):
		"""
		This Function grabs a card from a pack of cards
		"""
		card_popped = self.deck.pop()
		return card_popped


class Hand():
	"""
	This function describes what cards are in players Hand.
	It calculates the sum of those cards as well.
	"""
	def __init__(self):
		self.cards = []
		self.values = 0
		self.aces = 0

	def add_card(self,card):
		"""
		This Method takes in a card passed from Deck class
		deal() method and adds the value of that card to 
		self.value.
		"""
		# Appending the card drawn from Desk object to self.cards list
		self.cards.append(card)

		# Passing the rank of that card as a key to the values dictionary defined above
		# to get back the value associated with it and adding it to self.values. 

		self.values += values[card.ranks]

		# Track aces 
		if card.ranks == 'Ace':
			self.aces += 1

	def adjust_for_aces(self):
		"""
		If total value is greater than 21 and I still have an Ace
		then change my Ace to be 1 instead of 11
		"""
		while self.values > 21 and self.aces:
			self.values -= 10
			self.aces -= 1


class Chips():
	"""
	This class keeps the track of Player's starting chips,bets, and ongoing 
	winnings. 
	"""

	def __init__(self):
		self.total = 100
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def loss_bet(self):
		self.total -= self.bet


def take_bet(chips):
	"""
	This function takes in actual Bet value from the user
	"""
	while True:

		try:
			chips.bet = int(input("How many chips would you like to bet? "))
		except:
			# If the user didnt provide valid integer 
			print("Sorry Please provide an integer")
		else:
			# If the bet amount is greater than total chips 
			if chips.bet > chips.total:
				print(f"Sorry you do not have enough chips! You have: {chips.total}")
			else:
				break


def hit(deck,hand):
	"""
	This Function will take in Deck and Hand objects as an argument
	and basically will pop one card from the deck and add it to hand.
	"""
	# Pop the card from the Deck
	single_card = deck.deal()

	# Add that card in the Hand
	hand.add_card(single_card)

	#adjust the ace if required
	hand.adjust_for_aces()


def hit_or_stand(deck,hand):
	"""
	This Function will take in Deck and Hand objects as an argument
	and specify whether an user wants to draw another card or 
	wants to stand i.e let computer play its turn.
	"""
	# To control an upcoming while loop
	global playing

	while True:
		i = input('Hit or Stand? Enter h or s ')

		# Incase user enters 'Hit' or 'stand',checking the first letter of string
		if i[0].lower() == 'h':
			hit(deck,hand)

		elif i[0].lower() == 's':
			print("Player Stands, Dealer's Turn")
			playing = False

		# Incase users enters somethings that doesnt start with 'h' or 's'	
		else:
			print("Sorry!! I Do not understand that, Please enter h or s only!")
			continue

		break


def show_some(player,dealer):
	"""
	A Funtion to display all the player's card and dealer's card 
	except that one card of the dealer is hidden
	"""
	print("Dealer's Hand: ")
	print("One card Hidden!")
	print(dealer.cards[1])
	print('\n')
	print("Player's Hand: ")
	for card in player.cards:
		print(card)


def show_all(player,dealer):
	"""
	A Funtion to display all the player's card and dealer's card 
	"""
	print("Dealer's Hand: ")
	for card in dealer.cards:
		print(card)
	print('\n')
	print("Player's Hand: ")
	for card in player.cards:
		print(card)


def player_busts(player,dealer,chips):
	"""
	If the player is busted it will print out the message 
	and decrement the chips by calling loss_bet method
	"""
	print("BUST PLAYER!!!")
	chips.loss_bet()


def player_wins(player,dealer,chips):
	"""
	If the player wins it will print out the message 
	and increment the chips by calling win_bet method 
	"""
	print("PLAYER WINS!!!")
	chips.win_bet()


def dealer_busts(player,dealer,chips):
	"""
	If the dealer is busted it will print out the message 
	and increment the chips by calling win_bet method
	"""
	print("BUST DEALER, PLAYER WINS!!!")
	chips.win_bet()


def dealer_wins(player,dealer,chips):
	"""
	If the dealer wins it will print out the message 
	and decrement the chips by calling loss_bet method
	"""
	print("DEALER WINS!!!")
	chips.loss_bet()


def push(player,dealer):
	print("Dealer and Player tie! PUSH")


def black_jack():
	"""
	Actual Gameplay.
	"""
	global playing
	print("Welcome to BlackJack")

	# Create and Shuffle the Deck
	deck = Deck()
	deck.shuffle()

	# Deal two cards  to each player 

	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	# Set up player's chips
	player_chips = Chips()

	# Prompt the player for their bet
	take_bet(player_chips)

	# Show cards but keeping one dealer card hidden
	show_some(player_hand,dealer_hand)

	while playing:

		# Prompt the player to Hit or Stand
		hit_or_stand(deck,player_hand)

		# Show cards but keeping one dealer card hidden
		show_some(player_hand,dealer_hand)

	    # If player's hand exceeds 21, that means the player is busted 
	    # Run player_busts and exit the loop

		if player_hand.values > 21:
			player_busts(player_hand,dealer_hand,player_chips)
			break	


	# If the player hasnt busted, play Dealer's hand until Dealer reaches 17
	if player_hand.values <= 21:
		while dealer_hand.values < 17:
			hit(deck,dealer_hand)

		# Show all the cards
		show_all(player_hand,dealer_hand)

		# Different winning scenarios
		if dealer_hand.values > 21:
			dealer_busts(player_hand,dealer_hand,player_chips)
		elif dealer_hand.values > player_hand.values:
			dealer_wins(player_hand,dealer_hand,player_chips)
		elif dealer_hand.values < player_hand.values:
			player_wins(player_hand,dealer_hand,player_chips)
		else:
			push(player_hand,dealer_hand)

		# Inform the player of their chips total
		print("\n Player total chips are at: {}".format(player_chips.total))

		# Ask to play again 
		new_game = input("Do you want to play again? y/n ")

		if new_game[0].lower() == 'y':
			playing = True
			black_jack()
		else:
			print("Thank You for Playing!")
			
black_jack()