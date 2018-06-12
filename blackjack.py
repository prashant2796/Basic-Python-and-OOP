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

		self.values += values[card.rank]

		# Track aces 
		if card.rank == 'Ace':
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
