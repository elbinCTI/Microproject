import pickle as P
a=input("enter text to encode: ")
p=1
cs=list()
with open("enc1.bin", mode="rb") as f:
    while True:
        try:
            y=P.load(f)
            if y[0]=='ch':
                pass
            else:
                cs.append(y)
        except EOFError:
            break
for i in a:
    if i==' ':
        print(' ',end='')
        continue
    for r in cs:
        if r[0] == i:
            print(r[p], end="")
            p+=1
            break
    if p==63:
            p=1


