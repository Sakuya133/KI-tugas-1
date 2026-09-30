import os


# =========================
# Tabel DES
# =========================

IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

IP_INVERSE = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

S_BOXES = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]



def bytes_to_bits(data: bytes) -> str:
    return "".join(f"{byte:08b}" for byte in data)


def bits_to_bytes(bits: str) -> bytes:
    return bytes(
        int(bits[i:i + 8], 2)
        for i in range(0, len(bits), 8)
    )


def permute(bits: str, table: list[int]) -> str:
    return "".join(bits[position - 1] for position in table)


def left_rotate(bits: str, count: int) -> str:
    return bits[count:] + bits[:count]


def xor_bits(a: str, b: str) -> str:
    return "".join("0" if x == y else "1" for x, y in zip(a, b))


def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))



def generate_subkeys(key: bytes) -> list[str]:
    if len(key) != 8:
        raise ValueError("Key DES harus tepat 8 byte")

    key_bits = bytes_to_bits(key)
    key_56_bits = permute(key_bits, PC1)

    left = key_56_bits[:28]
    right = key_56_bits[28:]

    subkeys = []

    for shift in SHIFTS:
        left = left_rotate(left, shift)
        right = left_rotate(right, shift)

        subkey = permute(left + right, PC2)
        subkeys.append(subkey)

    return subkeys


def feistel(right: str, subkey: str) -> str:
    expanded = permute(right, E)
    mixed = xor_bits(expanded, subkey)

    sbox_result = ""

    for i in range(8):
        group = mixed[i * 6:(i + 1) * 6]

        row = int(group[0] + group[5], 2)
        column = int(group[1:5], 2)

        number = S_BOXES[i][row][column]
        sbox_result += f"{number:04b}"

    return permute(sbox_result, P)


def process_block(block: bytes, subkeys: list[str]) -> bytes:
    if len(block) != 8:
        raise ValueError("Satu blok DES harus tepat 8 byte")

    block_bits = bytes_to_bits(block)
    block_bits = permute(block_bits, IP)

    left = block_bits[:32]
    right = block_bits[32:]

    for subkey in subkeys:
        new_left = right
        new_right = xor_bits(left, feistel(right, subkey))

        left = new_left
        right = new_right


    result_bits = permute(right + left, IP_INVERSE)
    return bits_to_bytes(result_bits)


def encrypt_block(block: bytes, key: bytes) -> bytes:
    subkeys = generate_subkeys(key)
    return process_block(block, subkeys)


def decrypt_block(block: bytes, key: bytes) -> bytes:
    subkeys = generate_subkeys(key)
    return process_block(block, list(reversed(subkeys)))




def pad(data: bytes) -> bytes:
    padding_length = 8 - (len(data) % 8)
    return data + bytes([padding_length] * padding_length)


def unpad(data: bytes) -> bytes:
    if not data or len(data) % 8 != 0:
        raise ValueError("Data hasil dekripsi tidak valid")

    padding_length = data[-1]

    if padding_length < 1 or padding_length > 8:
        raise ValueError("Padding tidak valid")

    if data[-padding_length:] != bytes([padding_length] * padding_length):
        raise ValueError("Padding tidak valid; mungkin key salah")

    return data[:-padding_length]


def encrypt_message(plaintext: bytes, key: bytes) -> tuple[bytes, bytes]:
    if len(key) != 8:
        raise ValueError("Key DES harus tepat 8 byte")

    iv = os.urandom(8)
    data = pad(plaintext)

    previous = iv
    ciphertext = b""

    for i in range(0, len(data), 8):
        block = data[i:i + 8]
        mixed = xor_bytes(block, previous)
        encrypted = encrypt_block(mixed, key)

        ciphertext += encrypted
        previous = encrypted

    return iv, ciphertext


def decrypt_message(iv: bytes, ciphertext: bytes, key: bytes) -> bytes:
    if len(iv) != 8:
        raise ValueError("IV harus tepat 8 byte")

    if not ciphertext or len(ciphertext) % 8 != 0:
        raise ValueError("Panjang ciphertext tidak valid")

    previous = iv
    plaintext = b""

    for i in range(0, len(ciphertext), 8):
        block = ciphertext[i:i + 8]
        decrypted = decrypt_block(block, key)
        plaintext += xor_bytes(decrypted, previous)

        previous = block

    return unpad(plaintext)




if __name__ == "__main__":
    key = bytes.fromhex("133457799BBCDFF1")
    block = bytes.fromhex("0123456789ABCDEF")

    encrypted = encrypt_block(block, key)
    print("Tes satu blok:", encrypted.hex().upper())
    assert encrypted.hex().upper() == "85E813540F0AB405"
    assert decrypt_block(encrypted, key) == block

    message = "suki gedangan".encode("utf-8")

    iv, ciphertext = encrypt_message(message, key)
    decrypted = decrypt_message(iv, ciphertext, key)

    print("Plaintext  :", message.decode("utf-8"))
    print("IV         :", iv.hex())
    print("Ciphertext :", ciphertext.hex())
    print("Hasil buka :", decrypted.decode("utf-8"))