#!/usr/bin/python3
import english_scoring
import unittest

class EnglishScoringTest(unittest.TestCase):
    def test_frequency_table(self):
        sum = 0.0;
        for value in english_scoring.char_freq_dict.values():
            sum += value
        self.assertAlmostEqual(1.0, sum, places=4)

    def test_chi_squared_test(self):
        self.assertAlmostEqual(english_scoring.chi_squared_test(' '), 3.59548984093)
        self.assertAlmostEqual(english_scoring.chi_squared_test(' a'), 6.75084145404)
        self.assertAlmostEqual(english_scoring.chi_squared_test(' abcd'), 26.9184631726)

if __name__ == '__main__':
    unittest.main()
