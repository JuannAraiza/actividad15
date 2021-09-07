def main():
    #escribe tu código abajo de esta línea
    suma = 0

    n = int(input('Dame un número: '))

    while n != 0:
        suma = suma + n 
        n = int(input('Dame un número: '))

    print(suma) 


    

if __name__=='__main__':
    main()
