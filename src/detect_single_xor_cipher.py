#!/usr/bin/python3

import single_xor_cipher

def detect_single_xor_cipher(lines):
    min_score = float('inf')
    best_result = b''
    for line in lines:
        line = line.strip('\n')
        (result, score, best_key) = single_xor_cipher.solve_single_xor_cipher(bytearray.fromhex(line))
        if score < min_score:
            min_score = score
            best_result = result
    return (best_result, min_score)
