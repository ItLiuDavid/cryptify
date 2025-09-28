def caesarEncrypt():
    print("you are encrypting using caesar cipher")
    plaintext = list(input("write the desired plaintext: "))
    key = int(input("write the shift: "))
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
    print(ciphertext)
    return ciphertext

def caesarDecrypt():
    print("you are decrypting using caesar cipher")
    ciphertext = list(input("write the acquired cipher: "))
    key = int(input("write the shift: "))
    plaintext = ""
    for char in ciphertext:
        if char.islower(): 
            shift = (ord(char) - 97 - key) % 26 + 97
            plaintext += chr(shift)
        elif char.isupper():  
            shift = (ord(char) - 65 - key) % 26 + 65
            plaintext += chr(shift)
        else:
            plaintext += char
    print(plaintext)
    return ciphertext