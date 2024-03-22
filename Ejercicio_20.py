def tipo_triangulo(a, b, c):
    # Verificar si los lados forman un triángulo válido
    if a >= b + c or b >= a + c or c >= a + b:
        return "Los lados dados no forman un triángulo válido"
    
    # Verificar el tipo de triángulo
    if a == b == c:
        return "El triángulo es equilátero"
    elif a == b or a == c or b == c:
        return "El triángulo es isósceles"
    else:
        return "El triángulo es escaleno"

# Solicitar al usuario los lados del triángulo
a = float(input("Ingrese la longitud del lado a: "))
b = float(input("Ingrese la longitud del lado b: "))
c = float(input("Ingrese la longitud del lado c: "))

# Obtener el tipo de triángulo
tipo = tipo_triangulo(a, b, c)

# Mostrar el resultado
print(tipo)
