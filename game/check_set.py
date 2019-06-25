from random import choice

NUMBERS = [1,2,3]
SYMBOLS = ['DIAMOND','SQUIGGLE','OVAL']
SHADINGS = ['STRIPPED','SOLID', 'OPEN']
COLORS = ['RED','GREEN','PURPLE']

class Card:
	def __init__(self, number, symbol, shading, color):
		if any([
			number not in NUMBERS,
			symbol not in SYMBOLS,
			shading not in SHADINGS,
			color not in COLORS
		]):
			raise ValueError('Неправильные параметры карты')
	
		self.number = number
		self.symbol = symbol
		self.shading = shading
		self.color = color

	def __repr__(self):
		return f'{self.number} || {self.symbol} || {self.shading} || {self.color}'

def field_list(cards, field):
    return [getattr(card, field) for card in cards]

def check_set(cards):
	fields = ["number", "symbol", "shading", "color"]
	valid_len = (1,len(cards))
	return	all(
		len(set(field_list(cards,field))) in valid_len
		for field in fields
	)
	
def test():
	return 'Hello world'
	
# def generate_cards():
# 	return [Card(choice(NUMBERS),choice(SYMBOLS),choice(SHADINGS),choice(COLORS)) for i in range(3)]

# cards = [Card(1,'DIAMOND','SOLID','RED'), Card(2,'DIAMOND','SOLID','RED'),Card(1,'DIAMOND','SOLID','RED')]

# for card in cards:
# 	print(card)
# print(check_set(cards))