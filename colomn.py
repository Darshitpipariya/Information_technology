import math


def encryption():
    plaintext = input("Enter plaintext: ")
    plaintext = plaintext.replace(" ", "")
    key = input("Enter key: ")
    rows = math.ceil(len(plaintext)/len(key))
    position = 0
    m = []
    for i in range(rows):
        r = []
        for j in range(len(key)):
            if(position < len(plaintext)):
                r.append(plaintext[position])
            else:
                r.append("a")
            position += 1
        m.append(r)
    b = ""
    for i in range(1, len(key)+1):
        for j in range(rows):
            index = key.find(str(i))
            b += m[j][index]
    print(b)


def decryption():
    ciphertext = input("Enter ciphertext: ")
    key = input("Enter key: ")
    ciphertext = ciphertext.replace(" ", "")
    rows = math.ceil(len(ciphertext)/len(key))
    position = 0
    m = []
    for i in range(len(key)):
        r = []
        for j in range(rows):
            if(position < len(ciphertext)):
                r.append(ciphertext[position])
            else:
                r.append("a")
            position += 1
        m.append(r)
    rev_key = ""
    for i in range(1, len(key)+1):
        rev_key += str(key.find(str(i))+1)
    b = [["" for i in range(len(rev_key))] for j in range(rows)]
    for i in range(rows):
        for j in range(len(rev_key)):
            b[i][j] = m[j][i]
    b_s = [["" for i in range(len(rev_key))] for j in range(rows)]
    for i in range(1, len(key)+1):
        for j in range(rows):
            index = rev_key.find(str(i))
            b_s[j][i-1] = b[j][index]
    plaintext = ""
    for i in b_s:
        plaintext += "".join(i)
    print(plaintext)


if __name__ == "__main__":
    print("________ Columnar Transposition Cipher________")
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
