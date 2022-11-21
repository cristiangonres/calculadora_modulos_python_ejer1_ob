import operaciones.suma.suma
import operaciones.resta.resta
import operaciones.multiplicacion.multiplicacion
import operaciones.division.division
import operaciones.potencia.potencia


print("1 >> SUMA")
print("2 >> RESTA")
print("3 >> MULTIPLICACIÓN")
print("4 >> DIVISIÓN")
print("5 >> POTENCIA")
ope = input("¿Qué operación desea realizar? ")
match ope:
    case "1":
        contador = 0
        numeros = []
        while True:
            numero = int(input("Introduzca número a sumar: "))
            numeros.append(numero)
            contador += 1
            if contador >= 2:
                seguir = input("¿Desea continuar? (s/n): ")
                if seguir[0].lower() == 'n':
                    print(operaciones.suma.suma.suma(numeros))
                    break
    case "2":
        numero1 = int(input("Introduzca el minuendo: "))
        numero2 = int(input("Introduzca el sustraendo: "))
        print(operaciones.resta.resta.resta(numero1, numero2))
    case "3":
        contador = 0
        numeros = []
        while True:
            numero = int(input("Introduzca número a multiplicar: "))
            numeros.append(numero)
            contador += 1
            if contador >= 2:
                seguir = input("¿Desea continuar? (s/n): ")
                if seguir[0].lower() == 'n':
                    print(operaciones.multiplicacion.multiplicacion.multiplicacion(numeros))
                    break
    case "4":
        numero1 = int(input("Introduzca el dividendo: "))
        numero2 = int(input("Introduzca el divisor: "))
        print(operaciones.division.division.division(numero1, numero2))
    case "5":
        numero1 = int(input("Introduzca la base: "))
        numero2 = int(input("Introduzca exponente: "))
        print(operaciones.potencia.potencia.potencia(numero1, numero2))