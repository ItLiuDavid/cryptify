import math

def affineEncrypt(plaintext, a, b):
    if math.gcd(a, 26) != 1:
        raise ValueError("Multiplicative key 'a' is not coprime with 26, choose another.")
    ciphertext = ""
    for char in plaintext:
        if char.islower():
            x = ord(char) - 97
            shift = (a * x + b) % 26 + 97
            ciphertext += chr(shift)
        elif char.isupper():
            x = ord(char) - 65
            shift = (a * x + b) % 26 + 65
            ciphertext += chr(shift)
        else:
            ciphertext += char
    return ciphertext

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No modular inverse exists for this key.")

def affineDecrypt(ciphertext, a, b):
    if math.gcd(a, 26) != 1:
        raise ValueError("Multiplicative key 'a' is not coprime with 26, choose another.")
    a_inv = modinv(a, 26)
    plaintext = ""
    for char in ciphertext:
        if char.islower():
            y = ord(char) - 97
            shift = (a_inv * (y - b)) % 26 + 97
            plaintext += chr(shift)
        elif char.isupper():
            y = ord(char) - 65
            shift = (a_inv * (y - b)) % 26 + 65
            plaintext += chr(shift)
        else:
            plaintext += char
    return plaintext