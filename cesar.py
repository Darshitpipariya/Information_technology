def encrypt(msg, s):
    result = ""
    for str in msg.split():
        for i in str:
            if (i.isupper()):
                result += chr(((ord(i)+s-65) % 26)+65)
            else:
                result += chr(((ord(i)+s-97) % 26)+97)
        result+=" "
    return result


def decrypt(msg, s):
    result = ""
    for str in msg.split():
        for i in str:
            if (i.isupper()):
                result += chr((((ord(i)-s-65)+26) % 26)+65)
            else:
                result += chr((((ord(i)-s-97)+26) % 26)+97)
        result+=" "
    return result


print("________ Caesar cipher________")
choice=int(input("Enter choice\n1:Encryption\n2:Decryption\n"))
if (choice==1):
    s_msg = input("Enter plain text:-")
    print("\nencrypted message is {}".format(encrypt(s_msg,int(input("enter swap value ")))))
elif(choice==2):
    s_msg=input("Enter cipher text:-")
    print("\ndecrypted message is {}".format(decrypt(s_msg, int(input("enter swap value ")))))
else:
    print("Invalid choice")
