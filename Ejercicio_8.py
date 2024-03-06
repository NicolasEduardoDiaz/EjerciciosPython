#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.
print("hola usuario, soy un programa para leer la parte decimal de un numero")
print("por favor digita el numero decimal ")
numero = float(input("ingresa el numero decimal: "))
decimal = numero - (int(numero))
print(f"el numeor decimal de ",numero, "es ",decimal)