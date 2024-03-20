from math import*
import os
print(f"""
    __  __                             
   / / / /_  _____ _   ______          
  / /_/ / / / / _ \ | / / __ \         
 / __  / /_/ /  __/ |/ / /_/ /         
/_/ /_/\__,_/\___/|___/\____/          
  ___  ____     _________  ____  ____ _
 / _ \/ __ \   / ___/ __ \/ __ \/ __ `/
/  __/ / / /  / /__/ /_/ / /_/ / /_/ / 
\___/_/ /_/   \___/\____/ .___/\__,_/  
                       /_/             
""")

tamañoHuevo = int(input("Dime si el huevo es grande o pequeño, 1 para grande y 2 para pequeño: "))

if tamañoHuevo ==  1:
    
    thuevo = float(input("Ingrese la temperatura del huevo: "))
    m = 63 #Tamaño del huevo grande
    c = 3.7 #Capasidad calorifica especifica
    ro = 1.038 # Densidad 
    k = 0.0054 #conductividad termica
    tw = 100 #Temperatura de ebullicion del agua
    ty = 70 #Temperatura final 

    t = ((m**(2/3) * c * ro**(1/3)) / (k * pi**2 *((4 * pi)/3)**(2/3) ) * log( 0.76 * ((thuevo - tw)/(ty - tw)) ))
    print("El tiempo nescesario es ", t, "s")
elif tamañoHuevo == 2:
     
    thuevo = float(input("Ingrese la temperatura del huevo: "))
    m = 47 #Tamaño del huevo grande
    c = 3.7 #Capasidad calorifica especifica
    ro = 1.038 # Densidad 
    k = 0.0054 #conductividad termica
    tw = 100 #Temperatura de ebullicion del agua
    ty = 70 #Temperatura final 

    t = ((m**(2/3) * c * ro**(1/3)) / (k * pi**2 *((4 * pi)/3)**(2/3) ) * log( 0.76 * ((thuevo - tw)/(ty - tw)) ))
    print("El tiempo nescesario es ", t, "s")
else:
    ValueError
    print("Por favor ingresa un valor valido :3")
