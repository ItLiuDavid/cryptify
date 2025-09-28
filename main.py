import caesar

def main():
    print ("welcome to cryptify, what would you like to do?")
    while True:
        welcomeMessage()

def welcomeMessage():
    print ("1. Encrypt a message")
    print ("2. Decrypt a message")
    print ("3. Leave")
    choice = input("Enter 1 or 2: ")
    match choice:
        case "1":
            caesar.caesarEncrypt()
        case "2":
            caesar.caesarDecrypt()
        case "3":
            print("Great haxing mr racoon")
            quit()
        


if __name__ == "__main__":
    main()
