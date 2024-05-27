"""
1)Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una
cadena con un espacio adicional tras cada letra.
Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use
dicha función.

2)Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve
el valor máximo y el mínimo.

3)Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha
función en un programa principal que lea el radio de una circunferencia y muestre su área y
perímetro.

4)Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y
te devuelve Verdadero si el nombre de usuario es “usuario1”
y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado
hacer login y si no se ha podido hacer login incremente este valor.
Crear un programa principal donde se pida un nombre de usuario y una contraseña y se
intente hacer login, solamente tenemos tres oportunidades
para intentarlo.

5)Crear una función recursiva que permita calcular el factorial de un número. Realiza un
programa principal donde se lea un entero y se muestre el resultado
del factorial.

6)Crear una función que calcule el MCD de dos número por el método de Euclides. El método
de Euclides es el siguiente:
Se divide el número mayor entre el menor.
Si la división es exacta, el divisor es el MCD.
Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta
forma hasta obtener una división exacta, siendo el último divisor el MCD.
Crea un programa principal que lea dos números enteros y muestre el MCD.
"""
#**********************************************************************************************

import math


def convertirEspaciado(texto):
    textoEspaciado = ' '

    for i in range(len(texto)):
        textoEspaciado += texto[i] + ' '

    print(textoEspaciado)
    menuReturn = input("Presione Enter para regresar al menú principal...")
def calcularMaxMin(numeros):
    numMax = numeros[0]
    numMin = numeros[0]

    for i in numeros:
        if i > numMax:
            numMax = i

        if i < numMin:
            numMin = i

    print("El número menor ingresado es: {} y el número mayor es: {}".format(numMin, numMax))
    menuReturn = input("Presione Enter para regresar al menú principal...")

def login(userText, passText):
    if userText == "usuario1" and passText == "asdasd":
        return True

def areaPerimetro(radio):

    area = math.pi * radio**2
    perimetro = float(2 * math.pi * radio)

    print("El área del círculo es: {:.2f} unidades cuadradas y el perímetro es: {:.2f} unidades lineales".format(area, perimetro))
    menuReturn = input("Presione Enter para regresar al menú principal...")


def calculaMCD(n1, n2):
    mayor = 0
    menor = 0
    n1 = int(n1)
    n2 = int(n2)

    if n1 > n2:
        mayor = n1
        menor = n2

    else:
        mayor = n2
        menor = n1

    mcd = mayor % menor

    if mcd == 0:
        mcd = menor

    while mcd > 0:
        MCD = mcd
        mcd = mayor % mcd

    print("El MCD de {} es: {}".format(mayor, MCD))
    menuReturn = input("Presione Enter para regresar al menú principal...")

def factorial(num):
    if num == 1:
        return num
    else:
        num *= factorial(num - 1)
        return num


#**********************************************************************************************
# main

eleccion = 0

while eleccion == 0 or eleccion <= 6:
    print("╔==========================================================================╗")
    print("║ 1) reciba como parámetro un texto y devuelve una cadena con un espacio   ║")
    print("║    adicional tras cada letra.                                            ║")
    print("║ 2) Función “calcularMaxMin” que recibe una lista con valores numéricos   ║")
    print("║    y devuelve  el valor máximo y el mínimo.                              ║")
    print("║ 3) Subrutina llamada “Login”, que recibe un nombre de usuario y una      ║")
    print("║    contraseña y te devuelve Verdadero si el nombre de usuario es         ║")
    print("║    “usuario1” y la contraseña es “asdasd”                                ║")
    print("║ 4) Función que calcula el área y el perímetro de una circunferencia.     ║")
    print("║ 5) Crear una función recursiva que permita calcular el factorial de un   ║")
    print("║    número.                                                               ║")
    print("║ 6) Función que calcule el MCD de dos número por el método de Euclides    ║")
    print("╚==========================================================================╝")

    try:
        eleccion = int(input("Elija una opción del 1 al 6, para terminar, oprimir 'n', 'N': "))

        if eleccion == 1:
            cadena = input("Ingrese un texto para espaciarlo: ")
            convertirEspaciado(cadena)

        elif eleccion == 2:
            numList = []

            while True:
                try:
                    numero = int(input("Ingrese un número, para terminar captura, oprima otra tecla: "))
                    numList.append(numero)

                except:
                    break

            calcularMaxMin(numList)
            

        elif eleccion == 3:
            sesion = False
            intentos = 1
            usuario = input("Ingrese el usuario: ")
            password = input("Ingrese la contraseña: ")
            while intentos < 3:
                sesion = login(usuario, password)
                if sesion:
                    print("Verdadero: ")
                    break
                else:
                    print("Intente de nuevo, le quedan {} intentos". format(3-intentos))
                    intentos += 1
                    usuario = input("Ingrese el usuario: ")
                    password = input("Ingrese la contraseña: ")
            if not sesion:
                print("Número de intentos disponibles agotados, mejor suerte para la próxima")

            menuReturn = input("Presione Enter para regresar al menú principal...")

        elif eleccion == 4:
            radio = float(input("Ingrese el radio de la circinferencia: "))
            areaPerimetro(radio)

        elif eleccion == 5:
            resultado = 0
            valor = 0
            while True:
                try:
                    valor = int(input("Ingrese un número entero para calcular su factorial: "))
                    resultado = factorial(valor)
                    break

                except:
                    print("Debes ingresar un número entero, vuelve a intentarlo")

            print("El factorial de {}, es : {}".format(valor, resultado))
            menuReturn = input("Presione Enter para regresar al menú principal...")



        elif eleccion == 6:
            num1 = input("Ingrese el primer número para el cálculo del MCD: ")
            num2 = input("Ingrese el segundo número para el cálculo del MCD: ")
            calculaMCD(num1, num2)


    except ValueError:
        eleccion = 7
        print("Fin del multi-programa 1, gracias por ejecutarlo")