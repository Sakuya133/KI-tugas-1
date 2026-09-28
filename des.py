

IPtable = [58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7]


def permute(bits: str): 
    if (len(bits) != 64):
        print("kurang panjang or kepanjangan wok")
    else:
        permuteOutput = "".join(bits[pos - 1] for pos in IPtable)
    
    return permuteOutput

def left_rotate(bits, count): ...
def generate_subkeys(key: bytes): ...
def feistel(right, subkey): ...
def encrypt_block(block: bytes, key: bytes) -> bytes: ...
def decrypt_block(block: bytes, key: bytes) -> bytes: ...

def pad(data: bytes) -> bytes: ...
def unpad(data: bytes) -> bytes: ...
def encrypt_message(plaintext: bytes, key: bytes) -> tuple[bytes, bytes]: ...
def decrypt_message(iv: bytes, ciphertext: bytes, key: bytes) -> bytes: ...

if __name___ == "__main___":
    permute():