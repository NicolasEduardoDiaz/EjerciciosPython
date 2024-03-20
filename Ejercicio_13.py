#el resudio de una division
#es el cosiente por el divisor menos el dividendo 

print(f"""
    ____  _       _      _           
   / __ \(_)   __(_)____(_)___  ____ 
  / / / / / | / / / ___/ / __ \/ __ \
 / /_/ / /| |/ / (__  ) / /_/ / / / /
/_____/_/_|___/_/____/_/\____/_/ /_/ 
   / ____/  ______ ______/ /_____ _  
  / __/ | |/_/ __ `/ ___/ __/ __ `/  
 / /____>  </ /_/ / /__/ /_/ /_/ /   
/_____/_/|_|\__,_/\___/\__/\__,_/    
                                     
""")
print("Este programa sirve para ver si una division es exacta o inexacta")
print("Ingresa el dividendo y el divisor para calcular")
dividendo = int(input("Ingresa el dividendo: "))
divisor = int(input("Ingresa el divisor: "))

cosiente = dividendo / divisor
c1 = int(cosiente)

residuo =  dividendo-(c1 * divisor) 


if residuo == 0:
    print("La division es exacta:")
    print("cosiente: ", c1)
    print("residuo: ", residuo)
else:
    print("La division es INEXACTA:")
    print("cosiente: ", c1)
    print("residuo: ", residuo)
