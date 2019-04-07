#!/usr/bin/python3
import single_xor_cipher
import unittest

class SingleXORCipherTest(unittest.TestCase):
    def test(self):
        self.assertEqual(single_xor_cipher.solve_single_xor_cipher(
            '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'),
            'Cooking MC\'s like a pound of bacon')

if __name__ == '__main__':
    unittest.main()
