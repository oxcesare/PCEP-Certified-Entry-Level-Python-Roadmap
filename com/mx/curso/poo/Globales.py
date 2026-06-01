name ="global"

def asignarValor1():
    global name
    name = "valor asignado del metodo aasignarValor1"
    print(name)

def asignarValor2():
    global name
    name = "valor asignado del metodo aasignarValor2"
    print(name)

def asignarValor3():
    global name
    name = "valor asignado del metodo aasignarValor3"
    print(name)

def main():
    asignarValor1()
    asignarValor2()
    asignarValor3()

if __name__ == "__main__":
    main()