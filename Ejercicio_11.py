print(f"""
    ____                              
   / __ \____ ______                  
  / /_/ / __ `/ ___/                  
 / ____/ /_/ / /                      
/_/   _\__,_/_/                       
     / __ \                           
    / /_/ /                           
    \____/                        ___ 
   /  _/___ ___  ____  ____ _____/__ \
   / // __ `__ \/ __ \/ __ `/ ___// _/
 _/ // / / / / / /_/ / /_/ / /   /_/  
/___/_/ /_/ /_/ .___/\__,_/_/   (_)   
             /_/                      
""")
print("Este programa esta diseñado para calcular si un numero es par o impar")
numero = int(input("Por favor ingrese un número: "))

if numero % 2 == 0:
    print(numero, "es un numero par.")
else:
    print(numero, "NO es un numero par.")