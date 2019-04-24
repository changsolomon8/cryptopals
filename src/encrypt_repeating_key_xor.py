#!/usr/bin/python3

def encrypt_repeating_key_xor(text, key):
    key_index = 0
    raw_bytes = bytearray()
    for char in text:
        raw_bytes.append(ord(char) ^ ord(key[key_index]))
        key_index += 1
        if key_index > len(key) - 1:
            key_index = 0
    return raw_bytes.hex()
