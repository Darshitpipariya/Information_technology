def chr_freq(text):
    d={}
    for i in text:
        key=d.keys()
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

fre_alphabet=['e','t','a','o','i','n','s','r','h','d','l','u','c','m','f','y','w','g','p','b','v','k','x','q','']
text=input("enter text")
fre_text=chr_freq(text)
