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
