import PHCcore as phc

print("Project_Hyper_Cipher-VER 0.4 ")

while True:
    print("options:\n1. encode\n2. decode\n3. generate new sheet\n4. exit")
    op=int(input("\nenter option: "))
    match op:
        case 1:
            f=input("enter path of data sheet(.dat/.bin): ")# use enct.dat for testing
            if f.endswith('.dat') or f.endswith('.bin') == False:# path must end with .dat or .bin
                print("invalid file type")
                continue
            a=input("enter text to encode: ")
            phc.enc(a,f)
        case 2:
            f=input("enter path of data sheet(.dat/.bin): ")
            if f.endswith('.dat') or f.endswith('.bin') == False:
                print("invalid file type")
                continue
            a=input("enter text to decode: ")
            phc.dec(a,f)
        case 3:
            ns=input("enter path for new sheet (.dat/.bin): ")# path must end with .dat or .bin
            if ns.endswith('.dat') or ns.endswith('.bin') == False:
                print("invalid file type")
                continue
            phc.sheetgen(ns)
        case 4:
            break
        case _:
          print("invalid option")
