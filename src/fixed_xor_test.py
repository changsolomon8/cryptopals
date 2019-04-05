#!/usr/bin/python3
import fixed_xor
import unittest

class FixedXorTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fixed_xor.fixed_xor('1c0111001f010100061a024b53535009181c',
            '686974207468652062756c6c277320657965'),
            '746865206b696420646f6e277420706c6179')

if __name__ == '__main__':
    unittest.main()
