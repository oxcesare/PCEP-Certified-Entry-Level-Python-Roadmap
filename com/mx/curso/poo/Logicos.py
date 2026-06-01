def logicos():
    x =1
    if(x%2 ==0 or x%3==0):
        print("Es divisible por 2 o por 3")
    else:
        print("No es divisible por 2 ni por 3")

def logicos2():
    x =3
    y =2
    print(not x >y)

def main():
    logicos()
    logicos2()

if __name__ == "__main__":
    main()