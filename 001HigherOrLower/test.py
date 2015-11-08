import unittest
from guessadvisor import GuessAdviser

class HighOrLowTestCase(unittest.TestCase):
	def test_guess(self):
		ga = GuessAdviser()
		number = ga.number

		for guess in range(GuessAdviser.MIN, GuessAdviser.MAX):
			value = ga.guess(guess)
			if guess < number:
				self.assertEqual(value, GuessAdviser.HIGHER)
			if guess > number:
				self.assertEqual(value, GuessAdviser.LOWER)
			if guess is number:
				self.assertEqual(value, GuessAdviser.CORRECT)

if __name__ is '__main__':
	unittest.main()
