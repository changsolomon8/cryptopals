from itertools import combinations
import single_xor_cipher

def hamming_distance(one, two):
    assert(len(one) == len(two))
    distance = 0
    for i in range(len(one)):
        distance+=bin(one[i] ^ two[i]).count("1")
    return distance


def find_keysize(cipherbytes):
    MIN_KEYSIZE=2
    MAX_KEYSIZE=40
    result = []

    for keysize in range(MIN_KEYSIZE, MAX_KEYSIZE+1):
        chunks = []
        for i in range(0, len(cipherbytes), keysize):
            if i + keysize < len(cipherbytes):
                chunks.append(cipherbytes[i:i+keysize])

        distances = [hamming_distance(p[0], p[1]) / keysize  for p in combinations(chunks, 2)]
        avg_distance = sum(distances) / len(distances)
        result.append({
            'keysize': keysize,
            'avg_distance': avg_distance})

    return sorted(result, key = lambda x: x['avg_distance'])

# Return a keysize length list of the transposed blocks.
def generate_blocks(cipherbytes, keysize):
    results = [bytearray() for i in range(keysize)]

    for start_index in range(0, len(cipherbytes), keysize):
        for index in range(keysize):
            if start_index + index < len(cipherbytes):
                results[index].append(cipherbytes[start_index + index])
    return results

def decrypt_repeating_key_xor(cipherbytes):
    keysize = find_keysize(cipherbytes)[0]['keysize']

    blocks = generate_blocks(cipherbytes, keysize)

    final_key = ''
    single_solves = [single_xor_cipher.solve_single_xor_cipher(block) for block in blocks]
    for solve in single_solves:
        final_key += chr(solve[2])
    print(final_key)
