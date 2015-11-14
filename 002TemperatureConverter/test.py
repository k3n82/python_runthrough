import unittest
import tempconv

class TestTempConv(unittest.TestCase):
	def test_ctk(self):
		self.assertEqual(round(tempconv.ctk(-52), 2), 221.15)
		self.assertEqual(round(tempconv.ctk(122), 2), 395.15)

	def test_ctf(self):
		self.assertEqual(tempconv.ctf(-5.12), 22.784)
		self.assertEqual(tempconv.ctf(90), 194)

	def test_ftc(self):
		self.assertEqual(round(tempconv.ftc(-5.12), 2), -20.62)
		self.assertEqual(round(tempconv.ftc(90), 2), 32.22)

	def test_ftk(self):
		self.assertEqual(round(tempconv.ftk(-148), 2), 173.15)
		self.assertEqual(round(tempconv.ftk(500), 2), 533.15)

	def test_ktf(self):
		self.assertEqual(round(tempconv.ktf(100), 2), -279.67)

	def test_ktc(self):
		self.assertEqual(round(tempconv.ktc(500), 2), 226.85)

if __name__ is '__main__':
	unittest.main()
