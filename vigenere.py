#Vigenere uses a vector of k length to determine period length and also how many keys to shift.
#It is like a substitution cipher that changes every char within a specific period.
def vigenereEncrypt(plaintext, key):
    keyShift = []
    ciphertext = []
    for char in key: 
        if char.islower():
            keyShift.append(ord(char)-97)
        elif char.isupper():
            keyShift.append(ord(char)-65)
    for i, char in enumerate(plaintext):
        if char.islower():
            shift = (ord(char) - 97 + keyShift[i % len(keyShift)]) % 26 + 97
            ciphertext.append(chr(shift))
        elif char.isupper():
            shift = (ord(char) - 65 + keyShift[i % len(keyShift)]) % 26 + 65
            ciphertext.append(chr(shift))
        else:
            ciphertext.append(char)
    return "".join(ciphertext)

def vigenereDecrypt(ciphertext, key):
    keyShift = []
    plaintext = []
    for char in key:
        if char.islower():
            keyShift.append(ord(char)-97)
        elif char.isupper():
            keyShift.append(ord(char)-65)
    for i, char in enumerate(ciphertext):
        if char.islower():
            shift = (ord(char) - 97 - keyShift[i % len(keyShift)]) % 26 + 97
            plaintext.append(chr(shift))
        elif char.isupper():
            shift = (ord(char) - 65 - keyShift[i % len(keyShift)]) % 26 + 65
            plaintext.append(chr(shift))
        else:
            plaintext.append(char)
    return "".join(plaintext)


