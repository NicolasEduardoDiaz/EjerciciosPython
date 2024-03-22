def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."

def calculadora():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    operador = input("Introduce el operador (+, -, *, /): ")

    if operador == '+':
        print("Resultado:", suma(num1, num2))
    elif operador == '-':
        print("Resultado:", resta(num1, num2))
    elif operador == '*':
        print("Resultado:", multiplicacion(num1, num2))
    elif operador == '/':
        print("Resultado:", division(num1, num2))
    else:
        print("Operador no válido.")

calculadora()
