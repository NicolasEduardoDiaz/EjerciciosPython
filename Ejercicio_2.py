#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:
print("Hola ususario, soy un porgrama para calcular el area y el perimetro de un circulo, segun el radio")
radio = int(input("por favor ingresa el radio "))

area = 3.1416 * (radio**2)
perimetro = (2*3.1416)* radio

print("El area del circulo es ", area)
print("El perimetro del circulo es ", perimetro)