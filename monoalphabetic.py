def encrypt(msg,mono_dict):
    result=""
    for i in msg:
        result+=mono_dict[i]
    return result
def decrypt(msg,mono_dict_invers):
    result=""
    for i in msg:
        result+=mono_dict_invers[i]
    return result

print("________ Monoalphabetic cipher________")
mono_dict={'0':'A','1':'D','2':'C','3':'B','4':'E','5':'G','6':'H','7':'F','8':'I','9':'K','a':'J','b':'N','c':'O','d':'M','e':'L','f':'R','g':'Q','h':'P','i':'U','j':'S','k':'T','l':'X','m':'Z','n':'Y','o':'V','p':'W','q':'0','r':'2','s':'1','t':'3','u':'4','v':'7','w':'5','x':'9','y':'8','z':'6','A':'x','B':'z','C':'y','D':'w','E':'v','F':'q','G':'s','H':'r','I':'t','J':'u','K':'p','L':'a','M':'c','N':'d','O':'b','P':'e','Q':'h','R':'g','S':'f','T':'j','U':'i','V':'k','W':'n','X':'m','Y':'l','Z':'o',' ':' '}
mono_dict_invers=dict([(value, key) for key, value in mono_dict.items()])
choice=int(input("Enter choice\n1:Encryption\n2:Decryption\n"))
if (choice==1):
    s_msg = input("Enter plain text:-")
    print("\nencrypted message is {}".format(encrypt(s_msg,mono_dict)))
elif(choice==2):
    s_msg=input("Enter cipher text:-")
    print("\ndecrypted message is {}".format(decrypt(s_msg,mono_dict_invers)))
else:
    print("Invalid choice")
