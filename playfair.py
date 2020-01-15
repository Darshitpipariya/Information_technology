def key_genarator(key):
    alphabet='abcdefghiklmnopqrstuvwxyz'
    key=key.replace(" ","")
    table=[]
    for char in key.lower():
        if char not in table:
            if char=='j':
                char='i'
            table.append(char)
    for char in alphabet:
        if char not in table:
            table.append(char)
    j=0
    final=[]
    for i in range(5):
        l=[]
        for k in range(5):
            if(j<len(table)):
                l.append(table[j])
                j+=1
        final.append(l)
    return final


def to_diagraph(text):
    table=[]
    text=text.replace(" ","")
    for i in range(len(text)-1):
        table.append(text[i])
        if(text[i]==text[i+1]):
            if(text[i]=='x'):
                table.append('y')
            else:
                table.append('x')
    table.append(text[-1])
    if(len(table)%2!=0):
        if(text[-1]=='x'):
                table.append('y')
        else:
                table.append('x')
    l1=[]
    for i in range(0,len(table),2):
        l1.append([table[i],table[i+1]])
    return l1
    
def encryption():
    plaintext=input("Enter plaintext: " )
    key=input("Enter key: ")
    diagraph=to_diagraph(plaintext)
    key_matrix=key_genarator(key)
    cipher=[]
    #find co-ordinates of dia-graph in key metrix
    for d in diagraph:
        e1,e2=d[0],d[1]
        for i in range(len(key_matrix)):
            if(e1 in key_matrix[i]):
                j=key_matrix[i].index(e1)
                e1_x,e1_y=i,j
            if(e2 in key_matrix[i]):
                j=key_matrix[i].index(e2)
                e2_x,e2_y=i,j

        if(e1_x==e2_x):
            # if row is same
            e1=key_matrix[e1_x][(e1_y+1)%5]
            e2=key_matrix[e2_x][(e2_y+1)%5]    
        elif(e1_y==e2_y):
            # if column is same
            e1=key_matrix[(e1_x+1)%5][e1_y]
            e2=key_matrix[(e2_x+1)%5][e2_y]    
        else: 
            e1=key_matrix[e1_x][e2_y]
            e2=key_matrix[e2_x][e1_y]
        cipher.append(e1)
        cipher.append(e2)

    cipher="".join( i for i in cipher)
    print("Ciphertext:-{}".format(cipher))        

def decryption():
    ciphertext=input("Enter ciphertext: ")
    key=input("Enter key:")
    diagraph=to_diagraph(ciphertext)
    key_matrix=key_genarator(key)
    plaintext=[]
    #find co-ordinates of dia-graph in key metrix
    for d in diagraph:
        e1,e2=d[0],d[1]
        for i in range(len(key_matrix)):
            if(e1 in key_matrix[i]):
                j=key_matrix[i].index(e1)
                e1_x,e1_y=i,j
            if(e2 in key_matrix[i]):
                j=key_matrix[i].index(e2)
                e2_x,e2_y=i,j

        if(e1_x==e2_x):
            # if row is same
            e1=key_matrix[e1_x][(e1_y-1)%5]
            e2=key_matrix[e2_x][(e2_y-1)%5]    
        elif(e1_y==e2_y):
            # if column is same
            e1=key_matrix[(e1_x-1)%5][e1_y]
            e2=key_matrix[(e2_x-1)%5][e2_y]    
        else: 
            e1=key_matrix[e1_x][e2_y]
            e2=key_matrix[e2_x][e1_y]
        plaintext.append(e1)
        plaintext.append(e2)
        
    plaintext="".join( i for i in plaintext)
    plaintext=plaintext.replace('x','')
    print("Plaintext:- {} ".format(plaintext))

if __name__ == "__main__":
    print("________ Playfair cipher________")
    while True:
        choice=int(input("Enter choice\n1:Encryption\n2:Decryption\n3:Exit\n"))
        if (choice==1):
            encryption()
        elif(choice==2):
            decryption()
        elif(choice==3):
            break
        else:
            print("Invalid choice")
