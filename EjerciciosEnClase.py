import os
os.system('cls' if os.name == 'nt' else 'clear')

class EjerciciosEnClase:
    def __init__(self, nombre, perro, gato, a, b, Operacion, TotalCompra, Descuento, Isv, ValorCompra, SubTotal, Total, AnioActual, AnioNacimiento, Edad, TablaMultiplicar, Num, Diametro, MiPerro, Suma, Resta, Multi, Div, x, y, Potencia, Residuo, Raiz):
        self.nombre = nombre
        self.perro = perro
        self.gato = gato
        self.a = a
        self.b = b
        self.Operacion = Operacion
        self.TotalCompra = TotalCompra
        self.Descuento = Descuento
        self.Isv = Isv
        self.ValorCompra = ValorCompra
        self.SubTotal = SubTotal
        self.Total = Total
        self.AnioActual = AnioActual
        self.AnioNacimiento = AnioNacimiento
        self.Edad = Edad
        self.TablaMultiplicar = TablaMultiplicar
        self.Num = Num
        self.Diametro = Diametro
        self.MiPerro = MiPerro
        self.Suma = Suma
        self.Resta = Resta
        self.Multi = Multi
        self.Div = Div
        self.x = x
        self.y = y
        self.Potencia = Potencia
        self.Residuo = Residuo
        self.Raiz = Raiz

    def Condicionales(self):
        self.a = int(input("Ingrese un número: "))
        if self.a % 2 == 0:
            print(f"El numero {self.a} es par")
        else:
            print(f"El numero {self.a} es impar")

    def Ejercicio01(self):
        self.TotalCompra = 0
        self.Descuento = 0
        self.Isv = 0.15

        self.ValorCompra = float(input("Ingrese el valor de la compra por un producto: "))
        if self.ValorCompra >= 1000:
            self.Descuento = 0.25
        else:
            self.Descuento = 0
        self.TotalCompra = self.ValorCompra - (self.ValorCompra * self.Descuento)
        self.TotalCompra = self.TotalCompra + (self.TotalCompra * self.Isv)
        print(f"El total de la compra por un producto es: {self.TotalCompra}")

    def Ejercicio02(self):
        self.AnioActual = 2025
        self.AnioNacimiento = float(input("Por favor ingrese su año de nacimiento: "))
        self.Edad = self.AnioActual - self.AnioNacimiento

        print("Su edad actualmente es: ", self.Edad)

        if self.Edad >= 21:
            print("Usted es mayor de edad")
        else:
            print("Usted es menor de edad en el rango de los 21 años")
        
        if self.Edad >= 18:
            print("Usted es ciudadano, ya puede ejercer su derecho al voto")
        else:
            print("Usted es menor de edad, no puede ejercer su derecho al voto")

    def Ejercicio03(self):
        self.TablaMultiplicar = int(input("Por favor ingrese el numero de la tabla de multiplicar que quiere ver: "))
        print("TABLA DE MULTIPLICAR DEL", self.TablaMultiplicar)
        for i in range(1, 11):
            print(self.TablaMultiplicar, "x", i, "=", self.TablaMultiplicar * i)

    def Ejercicio04(self):
        self.i = 1
        self.Num = int(input("Por favor ingrese el numero de la tabla de multiplicar que desea ver: "))
        print("La tabla de multiplicar del ", self.Num, " es: ")
        while self.i <= 10:
            print(self.Num, "x", self.i, "=", self.Num * self.i)
            self.i += 1



