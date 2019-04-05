def fixed_xor(a, b):
    raw_bytes_a = bytearray.fromhex(a)
    raw_bytes_b = bytes.fromhex(b)

    for i in range(len(raw_bytes_a)):
        raw_bytes_a[i] ^= raw_bytes_b[i]
    return raw_bytes_a.hex()
