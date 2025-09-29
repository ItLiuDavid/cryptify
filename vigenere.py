#Vigenere uses a vector of k length to determine period length and also how many keys to shift.
#It is like a substitution cipher that changes every char within a specific period.

def vigenereEncrypt():
    print("you are encrypting using vigenere cipher")
    plaintext = list(input("write the desired plaintext: "))
    plaintextAscii = [ord(c) for c in plaintext]
    key = list(input("write the key: "))
    #asciiKey = [ord(c) for c in key]
    keyShift = []
    ciphertext = []
    for char in key:
        if char.islower():
            keyShift.append(ord(char)-97)
        elif char.isupper():
            keyShift.append(ord(char)-65)
    for i in plaintextAscii:
#            shift = (ord(char) - 97 + key) % 26 + 97
            ciphertext.append(plaintextAscii[i]+keyShift[i])

    print (ciphertext)
        




def vigenereDecrypt():
    print ("Test")


