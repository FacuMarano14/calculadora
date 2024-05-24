from os import system
from Funciones_Calculadora import *
flag_operando_a = False
flag_operando_b = False
seguir = True
a = None
b = None

while seguir == True:
    match menu(a, b):
        case "1":
            a = pedir_operando_a()
            flag_operando_a = True
        case "2":
            if not flag_operando_a:
                print("Comienze ingresando el primer numero")
            else: 
                b = pedir_operando_b()
                flag_operando_b = True
        case "3":
            if not flag_operando_a:
                print("No ingreso el primer numero")
                pausar()
            elif not flag_operando_b:
                print("No ingreso el segundo numero")
                pausar()
            else:
                resultado = suma(a, b)
                print(f"La suma de {a} y {b} da como resultado {resultado}")
        case "4":
            if flag_operando_a == False:
                print("No ingreso el primer numero")
                pausar()
            elif flag_operando_b == False:
                print("No ingreso el segundo numero")
                pausar()
            else:
                resultado = resta(a, b)
                print(f"La resta de {a} y {b} da como resultado {resultado}")
        case "5":
            if flag_operando_a == False:
                print("No ingreso el primer numero")
                pausar()
            elif flag_operando_b == False:
                print("No ingreso el segundo numero")
                pausar()
            else:
                resultado = multiplicacion(a, b)
                print(f"La multiplicacion de {a} y {b} da como resultado {resultado}")
        case "6":
            if flag_operando_a == False:
                print("No ingreso el primer numero")
                pausar()
            elif flag_operando_b == False:
                print("No ingreso el segundo numero")
                pausar()
            else:
                resultado = division(a, b)
                print(f"La division de {a} y {b} da como resultado {resultado}")
        case "7":
            if flag_operando_a == False:
                print("No ingreso el primer numero")
                pausar()
            elif flag_operando_b == False:
                print("No ingreso el segundo numero")
                pausar()
            else:
                factorial_a = factorial(a)
                factorial_b = factorial(b)
                print(f"El factorial de {a} es: {factorial_a} \nEl factorial de {b} es {factorial_b}")
        case "8":
            if desea_cerrar_programa("¿Desea cerrar la calculadora? si/no: "):
                seguir = False
                continue
    pausar()
    
print("Fin de la calculadora")