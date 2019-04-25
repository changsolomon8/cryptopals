import english_scoring

def solve_single_xor_cipher(raw_bytes):
    min_score = float('inf')
    best_result = b''
    best_key = -1

    for key in range(256):
        raw_string = ''
        for index in range(len(raw_bytes)):
            raw_string += chr(raw_bytes[index] ^ key)
        score = english_scoring.chi_squared_test(raw_string)
        if score < min_score:
            min_score = score
            best_result = raw_string
            best_key = key
    return (best_result, min_score, best_key)
