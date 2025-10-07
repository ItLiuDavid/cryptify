#Vigenere uses a vector of k length to determine period length and also how many keys to shift.
#It is like a substitution cipher that changes every char within a specific period.

def get_nonempty_input(prompt):
    while True:
        value = input(prompt)
        if value:
            return value
        print("Input cannot be empty, try again.")

def vigenereEncrypt():
    print("you are encrypting using vigenere cipher")
    plaintext = list(get_nonempty_input("write the desired plaintext: "))
    key = list(get_nonempty_input("write the key: "))
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
    print("".join(ciphertext))
        




def vigenereDecrypt():
    print ("Test")


