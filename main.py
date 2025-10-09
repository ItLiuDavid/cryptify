import caesar
import affine
import vigenere

def main():
    print ("welcome to cryptify, what would you like to do?")
    while True:
        welcomeMessage()

def welcomeMessage():
    print ("1. Encrypt a message")
    print ("2. Decrypt a message")
    print ("3. Leave")
    choice = input("Enter your choice ")
    match choice:
        case "1":
            encryptionMethods()
        case "2":
            decryptionMethods()
        case "3":
            print("Great haxing mr racoon")
            quit()
        
def encryptionMethods():
    print ("Caesar, Affine, Vigenere")
    choice = input("Pick your encryption method: ")
    match choice:
        case "1":
            print("you are encrypting using caesar cipher")
            plaintext = input("Enter plaintext: ")
            key = int(input("Enter key: "))
            ciphertext = caesar.caesarEncrypt(plaintext, key)
            print (ciphertext)
        case "2":
            print("you are encrypting using affine cipher")
            plaintext = input("write the desired plaintext: ")
            a = int(input("write the multiplicative key a: "))
            b = int(input("write the additive key b: "))
            ciphertext = affine.affineEncrypt(plaintext, a, b)
            print(ciphertext)
        case "3":
            print("you are encrypting using vigenere cipher")
            plaintext = input("write the desired plaintext: ")
            key = input("write the key: ")
            ciphertext = vigenere.vigenereEncrypt(plaintext, key)
            print(ciphertext)
        

        

def decryptionMethods():
    print ("Caesar, Affine, Vigenere")
    choice = input("Pick your Decryption method")
    match choice:
        case "1":
            print("you are decrypting using affine cipher")
            ciphertext = input("Enter ciphertext: ")
            key = int(input("Enter key: "))
            plaintext = caesar.caesarDecrypt(ciphertext, key)
            print (plaintext)
        case "2":
            print("You are decrypting using affine method")
            ciphertext = input("write the acquired ciphertext: ")
            a = int(input("write the multiplicative key a: "))
            b = int(input("write the additive key b: "))
            plaintext = affine.affineDecrypt(ciphertext, a, b)
            print(plaintext)
        case "3":
            print("you are decrypting using vigenere cipher")
            plaintext = input("write the acquired ciphertext: ")
            key = input("write the acquired key: ")
            plaintext = vigenere.vigenereDecrypt(plaintext, key)
            print(plaintext)


if __name__ == "__main__":
    main()
