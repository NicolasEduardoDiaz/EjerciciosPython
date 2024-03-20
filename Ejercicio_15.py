print(f"""
   ____           __                           _            __      
  / __ \_________/ /__  ____  ____ _____ ___  (_)__  ____  / /_____ 
 / / / / ___/ __  / _ \/ __ \/ __ `/ __ `__ \/ / _ \/ __ \/ __/ __ \
/ /_/ / /  / /_/ /  __/ / / / /_/ / / / / / / /  __/ / / / /_/ /_/ /
\____/_/   \__,_/\___/_/ /_/\__,_/_/ /_/ /_/_/\___/_/ /_/\__/\____/ 
                                                                    
""")
print("Este program sirve para organizar los numeros de menor a mayor")
print("ingresa los 4 numeros")

num1 = int(input("Ingresa el priemr numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))
num4 = int(input("ingresa el cuarto numero: "))
lista = [num1, num2, num3, num4]
lista.sort()

print("El orden de la lista es ",lista)