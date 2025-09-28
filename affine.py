import math
#In essence an affine cipher is a slightly more complicated caesar cipher

def affineEncrypt():
    print("you are encrypting using affine cipher")
    plaintext = input("write the desired plaintext: ")
    a = int(input("write the multiplicative key (a): "))
    b = int(input("write the additive key (b): "))
    if math.gcd(a,26)!=1: # necessary or else you can't decrypt the ciphertext. In essence it means that the function has to be invertible.
        print("Multiplicative key 'a' is not coprime with 26, choose another.")
        return affineEncrypt() 
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
    print(ciphertext)
    return ciphertext

def modinv(a, m): # Extended Euclidean Algorithm for modular inverse.
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No modular inverse exists for this key.")

def affineDecrypt():
    print("you are decrypting using affine cipher")
    ciphertext = input("write the acquired cipher: ")
    a = int(input("write the multiplicative key (a): "))
    b = int(input("write the additive key (b): "))
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
    print(plaintext)
    return plaintext