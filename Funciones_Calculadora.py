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
    """Resta el segundo valor ingresado al primero

    Args:
        operando_a (int): primer valor ingresado
        operando_b (int): segundo valor ingresado

    Returns:
        int: devuelve la resta del primer valor al segundo
    """
    return operando_a - operando_b
#---------------------------------------------------------------------
def multiplicacion(operando_a: int, operando_b: int)-> int:
    """multiplica los dos valores ingresados

    Args:
        operando_a (int): primer valor ingresado
        operando_b (int): segundo valor ingresado

    Returns:
        int: devuelve la multiplicacion de ambos valores
    """
    return operando_a * operando_b
#---------------------------------------------------------------------
def division(operando_a: int, operando_b: int)-> int:
    """divide los dos valores ingresados

    Args:
        operando_a (int): primer valor ingresado
        operando_b (int): segundo valor ingresado

    Raises:
        ZeroDivisionError: si uno de los dos valores ingresados es 0, no permite realizar la operacion

    Returns:
        int: Devuelve la division del primer numero ingresado por el segundo
    """
    if operando_a == 0 or operando_b == 0:
        raise ZeroDivisionError("No se puede dividir por 0")
    return operando_a / operando_b
#---------------------------------------------------------------------
def factorial(operando: int)-> int:
    """Permite calcular el factorial del valor ingresado

    Args:
        operando (int): valor del cual se quiere obtener el factorial

    Raises:
        ValueError: si el valor ingresado no es un numero natural no permite al usuario hacer el factorial

    Returns:
        int: devuelve el factorial del valor ingresado
    """
    fact = 1
    if operando < 0 :
        raise ValueError("El factorial es solo para numeros naturales")
    else:
        for i in range (1,operando + 1 ):
            fact *= i

    return fact
    
#---------------------------------------------------------------------
def limpiar_pantalla():
    """Limpia la pantalla
    """
    system("cls")
#---------------------------------------------------------------------
def pausar():
    """Pausa la animacion entre operaciones
    """
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
def desea_cerrar_programa(mensaje: str)-> str:
    """Le permite al usuario cerrar el programa

    Args:
        mensaje (str): pregunta al usuario si desea cerrar el programa

    Returns:
        str: si el usuario ingresa si, cierra el programa. Si ingresa no, continua.
    """
    rta = input(mensaje).lower()
    return rta == "si"

