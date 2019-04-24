import string

# https://www.codeproject.com/KB/security/Crack_Caesar_Cipher/1.jpg
char_freq_dict = {
    " " : 0.184820,
    "e" : 0.103320,
    "t" : 0.078395,
    "a" : 0.066284,
    "o" : 0.060091,
    "i" : 0.057941,
    "n" : 0.057526,
    "s" : 0.053997,
    "h" : 0.048210,
    "r" : 0.045744,
    "d" : 0.034530,
    "l" : 0.032366,
    "u" : 0.024719,
    "c" : 0.022742,
    "m" : 0.019853,
    "f" : 0.019242,
    "w" : 0.019183,
    "p" : 0.015438,
    "g" : 0.014424,
    "y" : 0.012656,
    "b" : 0.012026,
    "v" : 0.007474,
    "k" : 0.005482,
    "x" : 0.001466,
    "q" : 0.000851,
    "j" : 0.000667,
    "z" : 0.000555
}

puncuation = ',?!@#$%^&*()\'\"|{}./+-='

# Performs a chi squared test.  Smaller numbers are better.
def chi_squared_test(s):
    s = s.lower()
    # Build frequency dictionary.
    observed_freq = {}
    for c in s:
        if c not in observed_freq.keys():
            observed_freq[c] = 0
        observed_freq[c] += 1
    chi2 = 0.0
    for c in s:
        if c in char_freq_dict.keys():
            expected_count = char_freq_dict[c] * len(s)
            chi2 += (observed_freq[c] - expected_count) * (observed_freq[c] - expected_count) / expected_count
        elif c in string.printable:
            chi2 += len(s)
        else:
            chi2 += float('inf')
    return chi2

