"""
1) Hacer un programa donde se muestre el siguiente dibujo
* * * * * * * * * *
*                 *
*                 *
*                 *
* * * * * * * * * *

2) Hacer un programa que muestre el siguiente dibujo
*
* *
* * *
* * * *
* * * * *
3) Idem anterior con este dibujo
* * * * *
* * * *
* * *
* *
*

4)Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba
centrado en pantalla (suponiendo una anchura de 80 columnas;
pista: deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el mensaje
utilizando el carácter =.

5)Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es
múltiplo del otro. Crea una función EsMultiplo que reciba
los dos números, y devuelve si el primero es múltiplo del segundo.

6)Crear una función que calcule la temperatura media de un día a partir de la temperatura
máxima y mínima.
Crear un programa principal, que utilizando la función anterior, vaya pidiendo la
temperatura máxima y mínima de cada día y vaya mostrando la media.
El programa pedirá el número de días que se van a introducir.
"""

def imprimeMarco():
    for i in range(5):
        for j in range(10):
            if i == 0 or i == 4:
                print('* ', end = '')
            elif i > 0 or i < 4:
                if j == 0 or j == 9:
                    print('* ', end = '')
                else:
                    print('  ', end = '')
        print()
    menuReturn = input("Presione Enter regresar al menú principal...")

def imprimeTriangulo1():
    dec = 0
    for i in range(5):
        for j in range(5):
            print('*', end='')
            if dec - j == 0:
                break
        dec += 1
        print()
    menuReturn = input("Presione Enter regresar al menú principal...")

def imprimeTriangulo2():
    dec = 4
    for i in range(5):
        for j in range(5):
            print('*', end='')
            if dec - j == 0:
                break
        dec -= 1
        print()
    menuReturn = input("Presione Enter regresar al menú principal...")

def escribirCentrado():

    longitud = 80
    cadena = input("Ingresa un texto para ser centrado: ")
    espacio = int(40 - len(cadena) / 2)
    caracter = '=' * espacio

    print(caracter + cadena + caracter)

    menuReturn = input("Presione Enter regresar al menú principal...")

def esMultiplo():
    while True:
        print("Se deben ingresar dos números enteros, para determinar si el primeroes múltiplo del segundo")
        try:
            num1 = int(input("Ingrese el primer número: "))
            num2 = int(input("Ingrese el segundo número: "))
            break
        except ValueError:
            print("Uno o más valores ingresados son de tipo erroneo")

    multiplo = num1 % num2

    if multiplo == 0:
        print("{} es múltiplo de {}".format(num1, num2))

    else:
        print("{} no es múltiplo de {}".format(num1, num2))

    menuReturn = input("Presione Enter regresar al menú principal...")

def tempMedia(dias):
    tempMin = []
    tempMax = []
    mediaMin = 0
    mediaMax = 0
    sumMax = 0
    sumMin = 0
    for i in range(dias):
        print("Ingrese la temperatura mínima del día {}: ".format(i+1))
        tempMin.append(float(input()))
        sumMin += tempMin[i]
        print("Ingrese la temperatura máxima del día {}: ".format(i+1))
        tempMax.append(float(input()))
        sumMax += tempMax[i]

    media = ((sumMax + sumMin)/dias)/2
    print("La temperatura media durante los {} ingresados fue: {}ºC".format(dias, media,'.2f'))
    menuReturn = input("Presione Enter regresar al menú principal...")
#**********************************************************************************************
# main

eleccion = 0

while eleccion == 0 or eleccion <= 6:
    print("╔==========================================================================╗")
    print("║ 1) Programa donde que muestra el siguiente dibujo:                       ║")
    print("║                    * * * * * * * * * *                                   ║")
    print("║                    *                 *                                   ║")
    print("║                    *                 *                                   ║")
    print("║                    *                 *                                   ║")
    print("║                    * * * * * * * * * *                                   ║")
    print("║                                                                          ║")
    print("║ 2) Programa que muestre el siguiente dibujo:                             ║")
    print("║    *                                                                     ║")
    print("║    * *                                                                   ║")
    print("║    * * *                                                                 ║")
    print("║    * * * *                                                               ║")
    print("║    * * * * *                                                             ║")
    print("║                                                                          ║")
    print("║ 3) Idem anterior con este dibujo:                                        ║")
    print("║    * * * * *                                                             ║")
    print("║    * * * *                                                               ║")
    print("║    * * *                                                                 ║")
    print("║    * *                                                                   ║")
    print("║    *                                                                     ║")
    print("║                                                                          ║")
    print("║ 4) Función EscribirCentrado, que recibe como parámetro un texto y lo     ║")
    print("║    escribe centrado en pantalla (suponiendo una anchura de 80 columnas   ║")
    print("║    además subraya el mensaje utilizando el carácter '='.)                ║")
    print("║                                                                          ║")
    print("║ 5) Programa que pide dos número enteros al usuario y dice si alguno de   ║")
    print("║    ellos es múltiplo del otro. Crea una función EsMultiplo que reciba    ║")
    print("║    los dos números, y devuelve si el primero es múltiplo del segundo.    ║")
    print("║ 6) función que calcule la temperatura media de un día a partir de la     ║")
    print("║    temperatura máxima y mínima. El programa principal, que utilizando la ║")
    print("║    función anterior, vaya pidiendo la temperatura máxima y mínima de     ║")
    print("║    cada día y vaya mostrando la media. El programa pedirá el número de   ║")
    print("║    días que se van a introducir.                                         ║")
    print("╚==========================================================================╝")

    try:
        eleccion = int(input("Elija una opción del 1 al 6, para terminar, oprimir 'n', 'N': "))

        if eleccion == 1:
            imprimeMarco()

        elif eleccion == 2:
            imprimeTriangulo1()

        elif eleccion == 3:
            imprimeTriangulo2()

        elif eleccion == 4:
            escribirCentrado()

        elif eleccion == 5:
            esMultiplo()

        elif eleccion == 6:
            numDias = int(input("Ingresa la cantidad de días en los que se harán las mediciones de temperatura: "))
            tempMedia(numDias)

    except ValueError:
        eleccion = 7
        print("Fin del multi-programa 1, gracias por ejecutarlo")