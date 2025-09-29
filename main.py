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
            caesar.caesarEncrypt()
        case "2":
            affine.affineEncrypt()
        case "3":
            vigenere.vigenereEncrypt()
        

def decryptionMethods():
    print ("Caesar, Affine, Vigenere")
    choice = input("Pick your Decryption method")
    match choice:
        case "1":
            caesar.caesarDecrypt()
        case "2":
            affine.affineDecrypt()
        case "3":
            vigenere.vigenereDecrypt()


if __name__ == "__main__":
    main()
