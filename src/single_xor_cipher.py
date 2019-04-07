import english_scoring

def solve_single_xor_cipher(s):
    raw_bytes = bytearray.fromhex(s)
    min_score = float('inf')
    best_result = b''

    for key in range(256):
        raw_string = ''
        for index in range(len(raw_bytes)):
            raw_string += chr(raw_bytes[index] ^ key)
        score = english_scoring.chi_squared_test(raw_string)
        if score < min_score:
            min_score = score
            best_result = raw_string
    return best_result
