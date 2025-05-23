#snipet para limpiar la consola
import os
os.system('cls' if os.name == 'nt' else 'clear')

class EjerciciosTarea:
    def __init__(self, Num1, Num2, Num3, Sumatoria, Base, Altura, Area, Num):
        self.Num1 = Num1
        self.Num2 = Num2
        self.Num3 = Num3
        self.Sumatoria = Sumatoria
        self.Base = Base
        self.Altura = Altura
        self.Area = Area
        self.Num = Num

    #1 Imprime un saludo en la terminal
    def HolaMundo(self):
        print("Hola mundo soy Carlos Chávez y este es el primer programa de la tarea")

    #2 Suma dos numeros enteros
    def SumaDeDosNumeros(self):
        self.Num1 = int(input("Por favor ingrese el primer valor: "))
        self.Num2 = int(input("Por favor ingrese el segundo valor: "))
        self.Sumatoria = self.Num1 + self.Num2
        print(f"La suma de {self.Num1} y {self.Num2} es: {self.Sumatoria}")

    #3 Calcula el area de un rectangulo a partir de los datos que el usuario ingrese
    def CalcularAreaRectangulo(self):
        self.Base = int(input("Por favor ingrese la base del rectangulo: "))
        self.Altura = int(input("Por favor ingrese la altura del rectangulo: "))
        self.Area = self.Base * self.Altura
        print(f"El área del rectangulo es: {self.Area}")

    #4 Determina si un numero es positivo, negativo o cero
    def PositivoNegativoOCero(self):
        self.Num = int(input("Por favor ingrese un numero: "))
        if self.Num > 0:
            print(f"El numero que ingreso es positivo")
        elif self.Num < 0:
            print(f"El numero que ingreso es negativo")
        else:
            print(f"El numero que ingreso es cero")

    #5 Determina si un numero es par o impar
    def ParOImpar(self):
        self.Num = int(input("Por favor ingrese un numero: "))
        if self.Num % 2 == 0:
            print(f"El numero que ingreso es par")
        else:
            print(f"El numero que ingreso es impar")

    #6 Determina el mayor de tres numeros
    def MayorDeTresNumeros(self):
        self.Num1 = int(input("Por favor ingrese el primer numero: "))
        self.Num2 = int(input("Por favor ingrese el segundo numero: "))
        self.Num3 = int(input("Por favor ingrese el tercer numero: "))
        if self.Num1 > self.Num2 and self.Num1 > self.Num3:
            print(f"El mayor de los tres numeros es: {self.Num1}")
        elif self.Num2 > self.Num1 and self.Num2 > self.Num3:
            print(f"El mayor de los tres numeros es: {self.Num2}")
        else:
            print(f"El mayor de los tres numeros es: {self.Num3}")

    #7 Imprime los numeros del 1 al 10 usando un bucle for
    def ContadorUnoADiez(self):
        for i in range(1, 11):
            print("Numero: ", i)

    #8 Calcula la tabla de multiplicar de un numero ingresado por el usuario
    def TablaDeMultiplicar(self):
        self.Num = int(input("Por favor ingrese un numero: "))
        print("La tabla de multiplicar del numero", self.Num, "es: ")
        for i in range(1, 11):
            print(f"{self.Num} x {i} = {self.Num * i}")

    #9 Suma los primeros n numeros
    def SumarPrimerosNumeros(self):
        self.Num = int(input("Por favor ingrese un numero: "))
        self.Sumatoria = 0
        for i in range(1, self.Num + 1):
            self.Sumatoria += i
        print(f"La suma de los primeros {self.Num} numeros es: {self.Sumatoria}")

    #10 Dibuja una linea de asteriscos con la cantidad de asteriscos que el usuario ingrese
    def DibujoConAsteriscos(self):
        self.Num = int(input("Por favor ingrese un numero entero positivo: "))
        for i in range(1, self.Num + 1):
            print("*" * i)

