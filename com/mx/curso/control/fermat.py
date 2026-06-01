#Funcion de Fermat
def fermat(a,b,c):
    n=4
    if(n>2):
        if a**n + b**n == c**n:
            print("¡Fermat se equivocó!")
        else:
            print("No, esa combinación no funciona.")

def main():
    fermat(3,4,5)

if __name__ == "__main__":
    main()