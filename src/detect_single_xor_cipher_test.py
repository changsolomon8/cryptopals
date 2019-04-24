#!/usr/bin/python3
import detect_single_xor_cipher
import unittest

class DetectSingleXORCipherTest(unittest.TestCase):
    def test(self):
        f = open("../testdata/detect_single_xor_ciper_testdata.txt")
        f_lines = f.readlines();
        f.close()
        result = detect_single_xor_cipher.detect_single_xor_cipher(f_lines)
        self.assertEqual(result[0], 'Now that the party is jumping\n')
        self.assertAlmostEqual(result[1], 98.22511630508009)
        

if __name__ == '__main__':
    unittest.main()
