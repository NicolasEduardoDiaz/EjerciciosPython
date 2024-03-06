#Escriba un programa que pregunte al usuario la hora actual t del reloj 
#y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas
#Pedimos la hora actual y la cantidad de horas
print("Hola usuario, soy un programa para calcular la hora futura")
print("por favor ingresa los datos solicitados")
hora_actual = int(input("Hora actual: "))
cantidad_horas = int(input("Cantidad de horas: "))


hora_futura = (hora_actual+cantidad_horas) % 24
print ("En " ,(cantidad_horas)," horas, el reloj marcara las ",(hora_futura))