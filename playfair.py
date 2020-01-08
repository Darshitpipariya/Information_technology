k_ma = [['','','','',''] for i in range(5)]
def key_mat(key):
    k=0
    asc=97
    i=0
    while(i<5):
        j=0
        while(j<5):
            if len(key)>k:
                k_ma[i][j]=key[k]
                k+=1
                j+=1
            else:
                l1=[]
                for a in k_ma:
                    for b in a:
                        l1.append(b)
                print(l1)
                if( (chr(asc) not in l1 )and asc !=105 and asc!= 106):
                    k_ma[i][j]=chr(asc)
                    j+=1
                elif(((chr(105) not in l1) and (chr(106) not in l1))and (asc==105 or asc==106)):
                    k_ma[i][j]='i'
                    asc=107
                    j+=1
                else:
                    asc+=1
        i+=1
    return k_ma

# print(key_mat("darshit"))
#darshit
def diagraph(plaintext):
    l1=[]
    curent=0
    while(curent<len(plaintext)):
        l=['','']
        for j in range(2):
            if curent<len(plaintext):
                if()
                l[j]=plaintext[curent]
                curent+=1
        l1.append(l)
    print(l1)
diagraph("darshit")