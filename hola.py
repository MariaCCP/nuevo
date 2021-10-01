def pastel():
    ren=int(input("dime renglones: "))
    col=int(input("dime columndas: "))
    for i in range(1,ren+1):
        for j in range(1,col+1):
            print("*", end="")
        print("")

pastel()
