import random

class GuessAdviser:
	LOWER = 0
	HIGHER = 1
	CORRECT = True

	MIN=1
	MAX=100

	def __init__(self, number=None):
		if number == None:
			number = random.randint(self.MIN, self.MAX)
		self.number = number

	def guess(self, guess):
		""" If guess is higher than the number, return GuessAdviser.LOWER, if lower than number return GuessAdviser.HIGHER, else return GuessAdviser.CORRECT """
		if self.number < guess:
			return self.LOWER
		if self.number > guess:
			return self.HIGHER
		return self.CORRECT