n1 = int(input('Número 1:'))
n2 = int(input('Número 2:'))

seleccion = int(input("Escoge: (1) para sumar dos números, (2) para restar dos números, (3) para multiplicar dos números"))

if seleccion == 1:
    print (n1 + n2)
elif seleccion == 2:
    print (n1 - n2)
elif seleccion == 3:
    print (n1 * n2)
else:
    print ("Selección incorrecta")
