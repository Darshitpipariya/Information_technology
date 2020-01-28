def Encryption():
    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")
    ciphertext = ""
    plaintext = plaintext.replace(' ', '')
    key = key.replace(' ', '')
    pt = plaintext.lower()
    k = key.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(pt)):
        ciphertext += chr((alpha.index(pt[i]) +
                           alpha.index(k[i % len(k)])) % (26)+97)
    print(ciphertext)


def Decryption():
    ciphertext = input("Enter ciphertext: ")
    key = input("Enter key:")
    plaintext = ""
    ciphertext = ciphertext.replace(' ', '')
    key = key.replace(' ', '')
    ct = ciphertext.lower()
    k = key.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(ct)):
        plaintext += chr((alpha.index(ct[i]) -
                          alpha.index(k[i % len(k)])) % (26)+97)
    print(plaintext)


if __name__ == "__main__":
    print("________ Polyalphabetic cipher________")
    while True:
        choice = int(
            input("Enter choice\n1:Encryption\n2:Decryption\n3:Exit\n"))
        if (choice == 1):
            Encryption()
        elif(choice == 2):
            Decryption()
        elif(choice == 3):
            break
        else:
            print("Invalid choice")
