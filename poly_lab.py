def Encryption():
    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")
    ciphertext = ""
    pt = plaintext.replace(' ', '')
    k = key.replace(' ', '')
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
    upper_alpha = lower_alpha.upper()
    for i in range(len(pt)):
        if(pt[i].isupper() and k[i % len(k)].isupper()):
            ciphertext += chr((upper_alpha.index(pt[i]) +
                               upper_alpha.index(k[i % len(k)])) % (26)+65)
        if(pt[i].isupper() and k[i % len(k)].islower()):
            ciphertext += chr((upper_alpha.index(pt[i]) +
                               lower_alpha.index(k[i % len(k)])) % (26)+65)
        if(pt[i].islower() and k[i % len(k)].islower()):
            ciphertext += chr((lower_alpha.index(pt[i]) +
                               lower_alpha.index(k[i % len(k)])) % (26)+97)
        if(pt[i].islower() and k[i % len(k)].isupper()):
            ciphertext += chr((lower_alpha.index(pt[i]) +
                               upper_alpha.index(k[i % len(k)])) % (26)+97)
    print(ciphertext)


def Decryption():
    ciphertext = input("Enter ciphertext: ")
    key = input("Enter key: ")
    plaintext = ""
    ct = ciphertext.replace(' ', '')
    k = key.replace(' ', '')
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
    upper_alpha = lower_alpha.upper()
    for i in range(len(ct)):
        if(ct[i].isupper() and k[i % len(k)].isupper()):
            plaintext += chr((upper_alpha.index(pt[i]) +
                              upper_alpha.index(k[i % len(k)])) % (26)+65)
        if(ct[i].isupper() and k[i % len(k)].islower()):
            plaintext += chr((upper_alpha.index(pt[i]) +
                              lower_alpha.index(k[i % len(k)])) % (26)+65)
        if(ct[i].islower() and k[i % len(k)].islower()):
            plaintext += chr((lower_alpha.index(pt[i]) +
                              lower_alpha.index(k[i % len(k)])) % (26)+97)
        if(ct[i].islower() and k[i % len(k)].isupper()):
            plaintext += chr((lower_alpha.index(pt[i]) +
                              upper_alpha.index(k[i % len(k)])) % (26)+97)
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
