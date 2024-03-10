"""
Primera sesión de programas de autoaprendizaje
*******************************************************************************************
1) Hacer un programa donde se pida un nombre por teclado y se imprima “Hola
..el_nombre_ingresado”

2) Hacer un programa que solicite por teclado dos número y muestre la suma , la resta ,la
multiplicación y la división de esos números

3) Hacer un programa que solicite una edad e imprima “Es mayor” si es mayor de edad ,
sino que imprima “Es menor”.

4) Hacer un programa que solicite un color por teclado e imprima “Puede pasar “ si el
color ingresado es verde , “Precaución “ si es amarillo , “No pasar “ si es rojo o “Color
inválido” si es cualquier otro.

5) Hacer un programa que cuente desde el 1 al 100 y los imprima uno a uno.

6) Hacer un programa que cuente del 1 al 100 inclusive e imprima sólo los números pares

7) Hacer un programa que cuente del 1 al 100 inclusive e imprima los números que son
divisibles por 2 y por 5.

8) Hacer un programa que imprima una tabla de multiplicar del 2 al 9 . Cada uno debe
mostrar sus valores multiplicados del 1 al 9 inclusive

9) Hacer un programa que muestre el siguiente dibujo.
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
*******************************************************************************************
"""
def programa1(): #Esta simple función pide un nombre, y este se muestra
    nombre = input("Ingrese su nombre: ")
    print("Hola..", nombre)
    menuReturn = input("Presione Enter para regresar al menú principal...")
def programa2():    #Esta función pide dos números y muestra la suma, la resta,
                    #la multiplicación y la división
    num1 = int(input("Ingrese el primer número: "))
    while True: #En esta parte de la función, se implementa ese lazo infinito,para
                #validar que se ingrese un número mayor a cero, para evitar que
                #falle el programa.
        num2 = int(input("Ingrese el segundo número mayor a cero: "))
        if num2 > 0:
            break #Si num2 es mayor a cero se trunca el lazo infinito y sigue el
                  # flujo del programa
        else:
            print("el segundo número debe ser mayor a cero")

    print("La suma de {} y de {} es: {}".format(num1, num2, num1 + num2))
    print("La resta de {} y de {} es: {}".format(num1, num2, num1 - num2))
    print("La multiplicación de {} y de {} es: {}".format(num1, num2, num1 * num2))
    print("La división de {} y de {} es: {}".format(num1, num2, num1 / num2))
    menuReturn = input("Presione Enter para regresar al menú principal...")
def programa3():    #Esta función pide la edad y determina si se tiene mayoría de edad
    while True:
        edad = int(input("Ingresa tu edad: "))
        if edad > 0:
            break
        else:
            print("Debes ingresar una edad mayor a cero")

    if edad >= 0 and edad < 18:
       print("Eres menor de edad")
    else:
        print("Eres mayor de edad")
    menuReturn = input("Presione Enter para regresar al menú principal...")

def programa4(): #Esta subrutina pide uno de tres posiblers colores, a modo de semáforo

    colorInput = input("Ingrese un color 'v', 'V' para verde, 'a', 'A' para amarillo, "
                      "o 'r', 'R' para rojo: ")
    color = colorInput.upper()

    if color == 'V':
        print("Puede pasar")
    elif color == 'A':
        print("¡Precaución!")
    else:
        print("¡No pasar!")
    menuReturn = input("Presione Enter regresar al menú principal...")

def programa5():    #Función que imprime los números del 1 al 100
    for i in range(100):
        print(i + 1)
    menuReturn = input("Presione Enter regresar al menú principal...")

def programa6():     #Función que imprime los números pares del 1 al 100
    for i in range(1, 100):
        if i % 2 == 0:
            print(i)
    menuReturn = input("Presione Enter regresar al menú principal...")

def programa7():   # Función que imprime los números divisibles entre 2 y 5, del 1 al 100
    for i in range(1,100):
        if i % 2 == 0 or i % 5 == 0:
            print(i)
    menuReturn = input("Presione Enter regresar al menú principal...")

def programa8(): #Función que imprime las tablas de multiplicar del 2 al 9
    for i in range(1, 10):
        for j in range(1, 11):
            print("{} x {} = {}".format(i, j, i*j))
        print()
    menuReturn = input("Presione Enter regresar al menú principal...")

def programa9():    #Función que imprime una matríz del 5 x 10 del caracter '*'
    for y in range(5):
        for x in range(10):
            print('*', end = '')
        print()
    menuReturn = input("Presione Enter regresar al menú principal...")
#*****************************************************************************************
eleccion = 0

while eleccion == 0 or eleccion <= 10:
    print("╔==========================================================================╗")
    print("║ 1) Programa que pide un nombre por teclado e imprime                     ║")
    print("║    'Hola..el_nombre_ingresado'. Oprima 1 para ejecutarlo                 ║")
    print("║                                                                          ║")
    print("║ 2) Programa que solicita por teclado dos número y muestra la suma, la    ║")
    print("║    resta ,la multiplicación y la división de esos números. Oprima 2 para ║")
    print("║    ejecutarlo.                                                           ║")
    print("║ 3) Programa que solicita la edad y determine si es mayor de edad. Oprima ║")
    print("║    3 para ejecutarlo.                                                    ║")
    print("║ 4) Programa que pide un color por teclado e imprime “Puede pasar “ si el ║")
    print("║    color ingresado es verde , “Precaución “ si es amarillo , “No pasar “ ║")
    print("║    si es rojo o “Colorinválido” si es cualquier otro.                    ║")
    print("║ 5) Programa que cuenta desde el 1 al 100 y los imprima uno a uno         ║")
    print("║ 6) Programa que cuenta del 1 al 100 inclusive e imprima sólo los         ║")
    print("║    números pares                                                         ║")
    print("║ 7) Programa que cuenta del 1 al 100 inclusive e imprima los números que  ║")
    print("║    son divisibles por 2 y por 5.                                         ║")
    print("║ 8) Programa que imprime una tabla de multiplicar del 2 al 9 . Cada uno   ║")
    print("║    debe mostrar sus valores multiplicados del 1 al 9 inclusive           ║")
    print("║ 9) Programa que muestra el siguiente dibujo.                             ║")
    print("║    * * * * * * * * * *                                                   ║")
    print("║    * * * * * * * * * *                                                   ║")
    print("║    * * * * * * * * * *                                                   ║")
    print("║    * * * * * * * * * *                                                   ║")
    print("║    * * * * * * * * * *                                                   ║")
    print("╚==========================================================================╝")

    try:
        eleccion = int(input(" Elija una opción del 1 al 10, para terminar, oprimir 'n', 'N': "))
        if eleccion == 1:
            programa1()
        elif eleccion == 2:
            programa2()
        elif eleccion == 3:
            programa3()
        elif eleccion == 4:
            programa4()
        elif eleccion == 5:
            programa5()
        elif eleccion == 6:
            programa6()
        elif eleccion == 7:
            programa7()
        elif eleccion == 8:
            programa8()
        elif eleccion == 9:
            programa9()

    except ValueError:
        eleccion = 11
        print("Fin del multi-programa 1, gracias por ejecutarlo")