#!/usr/bin/python3
import hex_to_base64
import unittest

class HexToBase64Test(unittest.TestCase):
    def test(self):
        self.assertEqual(hex_to_base64.hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'), 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')
        self.assertEqual(hex_to_base64.hex_to_base64('4d616e'), 'TWFu')
        self.assertEqual(hex_to_base64.hex_to_base64('4d61'), 'TWE=')
        self.assertEqual(hex_to_base64.hex_to_base64('4d'), 'TQ==')
if __name__ == '__main__':
    unittest.main()
