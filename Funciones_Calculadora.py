from os import system
#---------------------------------------------------------------------
def pedir_operando_a()-> int:
    """Pide que se ingrese el primer numero

    Returns:
        int: primer numero
    """
    limpiar_pantalla()
    operando_a = int(input("Ingrese el primer operando: "))
    if operando_a != int:
        ValueError("Debe insertar un numero")
    return operando_a
#---------------------------------------------------------------------
def pedir_operando_b()->int:
    """Pide que se ingrese el segundo numero

    Returns:
        int: segundo numero
    """
    limpiar_pantalla()
    operando_b = int(input("Ingrese el segundo operando: "))
    if operando_b != int:
        ValueError("Debe insertar un numero")
    return operando_b
#---------------------------------------------------------------------
def suma(operando_a: int, operando_b: int)-> int:
    """Suma los dos numeros ingresados

    Args:
        operando_a (int): variable que contiene el primer numero
        operando_b (int): variable que contiene el segundo numero

    Returns:
        int: La suma de los dos numeros
    """
    return operando_a + operando_b
#---------------------------------------------------------------------
def resta(operando_a: int, operando_b: int)-> int:
    return operando_a - operando_b
#---------------------------------------------------------------------
def multiplicacion(operando_a: int, operando_b: int)-> int:
    return operando_a * operando_b
#---------------------------------------------------------------------
def division(operando_a: int, operando_b: int)-> int:
    if operando_a == 0 or operando_b == 0:
        raise ZeroDivisionError("No se puede dividir por 0")
    return operando_a / operando_b
#---------------------------------------------------------------------
def factorial(operando: int)-> int:
    fact = 1
    if operando < 0 :
        raise ValueError("El factorial es solo para numeros naturales")
    else:
        for i in range (1,operando + 1 ):
            fact *= i

    return fact
    
#---------------------------------------------------------------------
def limpiar_pantalla():
    system("cls")
#---------------------------------------------------------------------
def pausar():
    system("pause")
#---------------------------------------------------------------------
def menu(a:int,b:int)-> str:
    """_summary_

    Args:
        a (int): variable que contenga el primer valor
        b (int): variable que contenga el segundo valor

    Returns:
        Devuelve el menu de opciones con las variables a y b que corresponden al primer y segundo valor ingresado
    """
    limpiar_pantalla()
    print("Menu de opciones")
    print(f"1 - Primer valor (x = {a})")
    print(f"2 - Segundo valor (y = {b})")
    print("3 - Sumar")
    print("4 - Restar")
    print("5 - Multiplicar")
    print("6 - Dividir")
    print("7 - Factorial")
    print("8 - Cerrar Programa")
    opcion = input("Ingrese opcion: ")
    return opcion
#---------------------------------------------------------------------
def desea_cerrar_programa(mensaje: str)-> bool:
    rta = input(mensaje).lower()
    return rta == "si"

