import unittest
import tempconv

class TestTempConv(unittest.TestCase):
	def test_celsius_to_kelvin(self):
		self.assertEqual(round(tempconv.celsius_to_kelvin(-52), 2), 221.15)
		self.assertEqual(round(tempconv.celsius_to_kelvin(122), 2), 395.15)

	def test_celsius_to_fahrenheit(self):
		self.assertEqual(tempconv.celsius_to_fahrenheit(-5.12), 22.784)
		self.assertEqual(tempconv.celsius_to_fahrenheit(90), 194)

	def test_fahrenheit_to_celsius(self):
		self.assertEqual(round(tempconv.fahrenheit_to_celsius(-5.12), 2), -20.62)
		self.assertEqual(round(tempconv.fahrenheit_to_celsius(90), 2), 32.22)

	def test_fahrenheit_to_kelvin(self):
		self.assertEqual(round(tempconv.fahrenheit_to_kelvin(-148), 2), 173.15)
		self.assertEqual(round(tempconv.fahrenheit_to_kelvin(500), 2), 533.15)

	def test_kelvin_to_fahrenheit(self):
		self.assertEqual(round(tempconv.kelvin_to_fahrenheit(100), 2), -279.67)

	def test_kelvin_to_celsius(self):
		self.assertEqual(round(tempconv.kelvin_to_celsius(500), 2), 226.85)

if __name__ is '__main__':
	unittest.main()
