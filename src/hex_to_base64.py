#!/usr/bin/python3
from __future__ import division

def index_to_char(index):
    if index <= 25:
        return chr(ord('A') + index)
    if index <= 51:
        return chr(ord('a') + index - 26)
    if index <= 61:
        return chr(ord('0') + index - 52)
    if index == 62:
        return '+'
    else:
        return '/'
    


def hex_to_base64(s):
    # Each 4 bits is 1 hex digit.
    # Each 6 bits is 1 base64 digit.
    raw_bytes = bytes.fromhex(s)
    result_s = ''

    for i in range(max(1, int(len(raw_bytes) / 3))):
        mask = 0b11111100

        # First character
        char_0 = raw_bytes[3*i] & mask
        char_0 >>= 2
        char_0 = index_to_char(char_0)

        # Second character
        # Top 2 are from first octet
        mask = 0b00000011
        char_1 = (raw_bytes[3*i] & mask) << 4
        if 3*i + 1 < len(raw_bytes):
            char_1 |= (raw_bytes[3*i+1] & 0b11111000) >> 4
        char_1 = index_to_char(char_1)

        # Third character
        if 3*i + 1 >= len(raw_bytes):
            char_2 = '='
        else:
            mask = 0b00001111
            char_2 = (raw_bytes[3*i+1] & mask) << 2
            if 3*i + 2 < len(raw_bytes):
                char_2 |= (raw_bytes[3*i+2] & 0b11000000) >> 6
            char_2 = index_to_char(char_2)

        # Fourth character
        if 3*i + 2 < len(raw_bytes):
            char_3 = (raw_bytes[3*i+2] & 0b00111111)
            char_3 = index_to_char(char_3)
        else:
            char_3 = '='

        result_s += char_0 + char_1 + char_2 + char_3

    return result_s
