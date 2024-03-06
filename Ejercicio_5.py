#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso
print("Hola usuario soy un programa para invertir un numero de 3 digitos ")
numero = int(input("Ingresa el nuemro de 3 digitos "))

    
n1= numero//100 # Obtención del primer dígito
n2 = (numero // 10) % 10 # Obtención del segundo dígito
n3 = numero % 10 # Obtención del tercer dígito
numero_invertido = n3 * 100 + n2 * 10 + n1 
print(numero_invertido, " es el numero invertido ")
