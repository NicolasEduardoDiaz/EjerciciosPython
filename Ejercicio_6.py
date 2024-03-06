#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b
#de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c
#del triangulo, dado por el teorema de Pitágoras: c2=a2+b2

print("Hola usuario, soy un porgama para calcular la hipotenusa de un triangulo")
print("por favor ingresa los catetos")
a = int(input("cateto a "))
b = int(input("cateto b "))

c = (a**2 + b**2)**0.5
#c es la hipotenusa del triangulo
hipotenusa = c
print("la hipotenusa del triangulo es ", hipotenusa)