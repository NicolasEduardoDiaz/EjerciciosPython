print(f"""
    ____        __      __                          
   / __ \____ _/ /___ _/ /_  _________ _            
  / /_/ / __ `/ / __ `/ __ \/ ___/ __ `/            
 / ____/ /_/ / / /_/ / /_/ / /  / /_/ /             
/_/    \__,_/_/\__,_/_.___/_/_  \__,_/              
   ____ ___  ____ ______   / /___ __________ _____ _
  / __ `__ \/ __ `/ ___/  / / __ `/ ___/ __ `/ __ `/
 / / / / / / /_/ (__  )  / / /_/ / /  / /_/ / /_/ / 
/_/ /_/ /_/\__,_/____/  /_/\__,_/_/   \__, /\__,_/  
                                     /____/         
""")
print("Este codigo sirve para saber cual palabra es la mas larga")
print("Por favor ingresa las dos palabras")
palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

largo1 = len(palabra1)
largo2 = len(palabra2)

if largo1 > largo2:
    print("La palabra", palabra1, "tiene", (largo1 - largo2), "letras mas que", palabra2)
elif largo2 > largo1:
    print("La palabra", palabra2, "tiene", (largo2 - largo1), "letras mas que", palabra1)
else:
    print("Las dos palabras tienen el mismo largor")