#!/usr/bin/python3
import base64
import decrypt_repeating_key_xor
import unittest

class DecryptRepeatingKeyOXORTest(unittest.TestCase):
    def testHamming(self):
        self.assertEqual(
                decrypt_repeating_key_xor.hamming_distance(
                    bytearray('this is a test', 'utf-8'),
                    bytearray('wokka wokka!!!', 'utf-8')), 37)

    def test(self):
        f = open('../testdata/decrypt_repeating_key_xor.txt')
        content = f.read()
        f.close()
        #self.assertEqual(decrypt_repeating_key_xor.find_keysize(base64.b64decode(content))[0]['keysize'], 29)
        decrypt_repeating_key_xor.decrypt_repeating_key_xor(base64.b64decode(content))




if __name__ == '__main__':
    unittest.main()
