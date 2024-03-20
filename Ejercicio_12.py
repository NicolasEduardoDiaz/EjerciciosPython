#Aquellos años que son divisibles entre 4,
# pero no entre 100, son bisiestos. Los años que son divisibles entre 100, 
#pero no entre 400, no son bisiestos
print(f"""
    ___     /\//                        
   /   |  _//\/ ____                    
  / /| | / __ \/ __ \                   
 / ___ |/ / / / /_/ /                   
/_/ _|_/_/ /_/\____/            __      
   / __ )_____(_)_______  _____/ /_____ 
  / __  / ___/ / ___/ _ \/ ___/ __/ __ \
 / /_/ (__  ) (__  )  __(__  ) /_/ /_/ /
/_____/____/_/____/\___/____/\__/\____/ 
                                        
""")
print("Este es un programa para ver si un año es bisiesto o no ")
año = int(input("Ingresa el año que deseas averiguar: ")) #el año que queremos comprobar

if año % 4 != 0: #no divisible entre 4
	print(año, "No es bisiesto")
elif año % 4 == 0 and año % 100 != 0: #divisible entre 4 y no entre 100 o 400
	print(año, "Es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: #divisible entre 4 y 10 y no entre 400
	print(año, "No es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: #divisible entre 4, 100 y 400
	print(año, "Es bisiesto")