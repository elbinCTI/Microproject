import csv as c
a=input("enter text to decode: ")
p=1
with open("C:\\Users\\elbin\\OneDrive\\Desktop\\hc\\ds2.csv", mode="r") as f:
    reader=c.reader(f)  
    next(reader) 
    for i in a:
        if i==' ':
            print(' ',end='')
        for r in reader:
            if r[p] == i:
                print(r[0], end="")
                p+=1
                break
        if p==63:
            p=1
        f.seek(0)
        next(reader)
