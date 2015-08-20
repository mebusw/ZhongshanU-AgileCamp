import math
import unittest

def rabbit(n):
	a = -1; b = 1;
	for i in range(n):
		a += b
		t = a
		a = b
		b = t
	return b

class ATest(unittest.TestCase):
	def test_rabbit(self):
		self.assertEqual(3, rabbit(1))

if __name__ == '__main__':
	unittest.main()