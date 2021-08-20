import random
from termcolor import colored
from pyfiglet import figlet_format
class Card:
	def __init__(self,value,suit):
		self.value = value
		self.suit = suit
	def __repr__(self):
		return f"{self.suit} {self.value}"
	def execute(self):
		return None
	def __eq__(self,other):
		return all((isinstance(other, self.__class__),
			self.suit == other.suit,
			self.value == other.value))

class Deck:
	def __init__(self):
		suits = ["Hearts","Clubs","Spades","Diamonds"]
		values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
		self.cards = [Card(value,suit) for value in values for suit in suits]
	def __repr__(self):
		return f"Deck of {self.count()}"
	def count(self):
		return len(self.cards)
	def shuffle(self):
		if self.count() < 52:
			raise ValueError ("Sorry, only full decks can be shuffled.")
		random.shuffle(self.cards)
		return self
	def _deal(self,num_of_cards_to_be_dealt):
		if self.count() == 0:
			raise ValueError ("Sorry, this deck has no cards remaining.")
		actual = min(self.count(),num_of_cards_to_be_dealt)
		dealt_cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		return dealt_cards
	def deal_hand(self,hand_size = 4):
		return self._deal(hand_size)
figlettext = figlet_format ("Bastra","slant")
colortext = colored(figlettext,"cyan")
print(colortext)
deste = Deck()
kar_deste = deste.shuffle()


orta = (kar_deste.deal_hand())

print(f"The card in the middle: {orta[-1]}")
user_score = 0
comp_score = 0
while kar_deste.count() != 0:
	computer_hand = kar_deste.deal_hand()
	user = kar_deste.deal_hand()
	print(f"Your cards: {user}")
	while len(user) != 0:
		card_number = None
		while card_number not in [1,2,3,4]:
			card_number=int(input("Please choose a card (1-4)."))
			if card_number not in (1,2,3,4):
				print("Please make a valid move.")
		real_card_number= int(card_number) - 1
		user_turn = user[real_card_number]
		del user[real_card_number]
		orta.append(user_turn)
		if len(orta) != 1:
			if len(orta) == 2:
				if orta[-2].value == user_turn.value:
					user_score += 10
					orta = []
					user_turn = None
					print("Congrats bastra! 10 points")
				else:
					user_turn = None
			elif user_turn.value == "J":
				if len(orta) > 1:
					print("Score! 1 point.")
					user_score += 1
					orta = []
				else:
					user_turn = None
			elif orta[-2].value == user_turn.value:
					print("Score! 1 point.")
					user_score +=1
					user_turn = None
					orta = []
			else:
				user_turn = None
		if len(orta) != 0:
			print(f"The card in the middle: {orta[-1]} ")
		else:
			print("There are no cards left in the middle.")
		computer_turn = random.choice(computer_hand)
		computer_hand.remove(computer_turn)
		print(f"The computer made its move: {computer_turn}")
		orta.append(computer_turn)
		if len(orta) != 1:
			if len(orta) == 2 :
				if orta[-2].value == computer_turn.value:
					comp_score += 10
					orta = []
					computer_turn = None
					print("Bastra! 10 points for the computer.")
				else:
					computer_turn = None

			elif computer_turn.value == "J":
				if len(orta) > 1:
					print("Score! 1 point for the computer.")
					comp_score += 1
					orta = []
				else:
					computer_turn = None
			elif orta[-2].value == computer_turn.value:
					comp_score += 1
					print("Score! 1 point for the computer.")
					computer_turn = None
					orta = []
			else:
				computer_turn = None
		if len(orta) != 0:
			print(f"The card in the middle: {orta[-1]} ")
		else:
			print("There are no cards left in the middle.")
		print(f"Your cards: {user}")

print(f"Your score: {user_score}, computer's score: {comp_score}")

			
