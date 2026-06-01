
def funcionEjemplo():
    print("funcionEjemplo")
    #ejemplo de uso del do while
    i=0
    while True:
        print(i)
        i+=1
        if i>5:
            break

def main():
    funcionEjemplo()

if __name__ == "__main__":
    main()