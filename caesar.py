def caesarEncrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.islower(): 
            shift = (ord(char) - 97 + key) % 26 + 97
            ciphertext += chr(shift)
        elif char.isupper():  
            shift = (ord(char) - 65 + key) % 26 + 65
            ciphertext += chr(shift)
        else:
            ciphertext += char
    return ciphertext

def caesarDecrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.islower(): 
            shift = (ord(char) - 97 - key) % 26 + 97
            plaintext += chr(shift)
        elif char.isupper():  
            shift = (ord(char) - 65 - key) % 26 + 65
            plaintext += char
        else:
            plaintext += char
    return plaintext