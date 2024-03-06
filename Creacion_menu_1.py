#Calificador de programas
#Primero se definen las opciones que el usuario seleccionara en el menu
def imprimir(variable):
    print(variable)
def sumar(a, b):
    return a + b
def calcular_edad(fecha_nac):
    return date.today() - fecha_nac
def IMC(Masa, Estatura):
    return Masa/(Estatura**2)
def Hallarparesoimpares(n):
    if n % 2 == 0:
        print(n, "es par.")
    else:
        print(n, "es impar.")

def Areacuadrado(l):
    return l1**2
def Areatriangulo(b, h):
    return b * h / 2

def Mayordeedad(edad):
     if edad >= 18:
        print("Es mayor de edad")
     else:
        print("No es mayor de edad")

def Aumentosalario(salario_actual, salario_pasado):
     if salario_actual-salario_pasado > 0:
        print("Aumento de salario")
     else:
        print("No aumento de salario")
def Pagodehorasextras(HJL,HL):#HJL=Horas jornada laboral #HL=Horas laboradas
    if HL > HJL:
        print("Paga la hora extra")
    else:
        print("No paga la hora extra")

def mostrar_menu():
    print("selecciona una operacion")
    print("1.Hola mundo")
    print("2. Sumar")
    print("3. Calcular edad")
    print("4. IMC")
    print("5. Hallar pares o impares")
    print("6. Area cuadrada")
    print("7. Area triangulo")
    print("8. Mayor de edad")
    print("9.Aumento de salario")
    print("10.Pagar hora extra")
    print("11. Salir")


def main():

    mostrar_menu()

    opcion = input("Ingrese el número correspondiente a la operación deseada: ")
    if opcion == '1':
        variable = input("Ingrese una variable")
        imprimir(variable)
    elif opcion == "2":
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        resultado = sumar(a, b)
        print(f"Resultado: {resultado}")
    elif opcion == "3":
        fecha_nac = int(input("Ingrese la fecha de nacimiento: "))
        edad = calcular_edad(fecha_nac)
        print(f"La edad es: {edad}")
    elif opcion == "4":
        Masa = float(input("Ingrese la masa corporal: "))
        Estatura = float(input("Ingrese la estatura: "))
        IMC = IMC(Masa,Estatura)
        print(f"El IMC es: {IMC(Masa,Estatura)}")
    elif opcion == "5":
        n = int(input("Ingrese un número entero: "))
        if n % 2 == 0:
            print(n, "es par.")
        else:
            print(n, "es impar.")
    elif opcion == "6":
        l = int(input("Ingrese un número entero: "))
        print(f"Resultado: {l}")
    elif opcion == "7":
        b = int(input("Ingrese un número entero: "))
        h = int(input("Ingrese un número entero: "))
        resultado = Areatriangulo(b, h)
        print(f"Resultado: {resultado}")
    elif opcion == "8":
        edad = int(input("Ingrese la edad: "))
        Mayordeedad(edad)
    elif opcion == "9":
        salario_actual = int(input("Ingrese el salario actual: "))
        salario_pasado = int(input("Ingrese el salario pasado: "))
        Aumentosalario(salario_actual, salario_pasado)
    elif opcion == "10":
        HJL = int(input("Ingrese la hora jornada laboral: "))
        HL = int(input("Ingrese la hora laborada: "))
        Pagodehorasextras(HJL,HL)
    elif opcion == "11":
        print("Saliendo")
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 11")

if __name__ == "__main__":
    while True:
     main()

