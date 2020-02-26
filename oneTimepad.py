def encryption():
    plaintext = input("Enter plaintext").lower()
    key = input("Enter key").lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    while(len(plaintext) != len(key)):
        key = input("Enter valid key").lower()
    for i in range(len(plaintext)):
        c = alphabet.find(plaintext[i]) ^ alphabet.find(key[i])
        ciphertext += alphabet[c % 26]
    print(ciphertext)


def decryption():
    plaintext = input("Enter Ciphertext").lower()
    key = input("Enter key").lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    while(len(plaintext) != len(key)):
        key = input("Enter valid key").lower()
    for i in range(len(plaintext)):
        c = alphabet.find(plaintext[i]) ^ alphabet.find(key[i])
        ciphertext += alphabet[c % 26]
    print(ciphertext)


if __name__ == "__main__":
    print("________ One time pad Cipher________")
    while True:
        choice = int(
            input("Enter choice\n1:Encryption\n2:Decryption\n3:Exit\n"))
        if (choice == 1):
            encryption()
        elif(choice == 2):
            decryption()
        elif(choice == 3):
            break
        else:
            print("Invalid choice")
