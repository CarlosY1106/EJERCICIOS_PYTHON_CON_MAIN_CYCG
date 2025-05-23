#snipet para limpiar la consola
import os
os.system('cls' if os.name == 'nt' else 'clear')

from EjerciciosTarea import EjerciciosTarea

Respuestas = EjerciciosTarea(Num1=0, Num2=0, Num3=0, Sumatoria=0, Base=0, Altura=0, Area=0, Num=0)

print("Ejercicio 01 - Imprime un saludo en la terminal")
Respuestas.HolaMundo()

print("Ejercicio 02 - Suma dos numeros enteros")
Respuestas.SumaDeDosNumeros()

print("Ejercicio 03 - Calcula el area de un rectangulo a partir de los datos que el usuario ingrese")
Respuestas.CalcularAreaRectangulo()

print("Ejercicio 04 - Determina si un numero es positivo, negativo o cero")
Respuestas.PositivoNegativoOCero()

print("Ejercicio 05 - Determina si un numero es par o impar")
Respuestas.ParOImpar()

print("Ejercicio 06 - Determina el mayor de tres numeros")
Respuestas.MayorDeTresNumeros()

print("Ejercicio 07 - Imprime los numeros del 1 al 10 usando un bucle for")
Respuestas.ContadorUnoADiez()

print("Ejercicio 08 - Calcula la tabla de multiplicar de un numero ingresado por el usuario")
Respuestas.TablaDeMultiplicar()

print("Ejercicio 09 - Suma los primeros n numeros")
Respuestas.SumarPrimerosNumeros()

print("Ejercicio 10 - Dibuja una linea de asteriscos con la cantidad de asteriscos que el usuario ingrese")
Respuestas.DibujoConAsteriscos()