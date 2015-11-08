import string
import unittest
import namegen

class NameGenTestCase(unittest.TestCase):
	def is_name(self, name):
		alphabets = list(string.ascii_lowercase)
		vowels = ['a','e','i','o','u','y']
		constants = [i for i in alphabets if i not in vowels]

		vowel_count = 0
		constant_count = 0
		for i in name:
			if vowel_count > 2 or constant_count > 1:
				return False
			if i in vowels:
				vowel_count += 1
				constant_count = 0
				continue
			if i in constants:
				constant_count += 1
				vowel_count = 0

		return True

	def test_generate_name(self):
		for i in range(0,10):
			self.assertTrue( self.is_name(namegen.generate_name()) )
		for i in range(0,10):
			for x in range(0,10):
				for y in range(0,10):
					self.assertTrue(self.is_name(namegen.generate_name(x, x + y)))


if __name__ == '__main__':
    unittest.main()
