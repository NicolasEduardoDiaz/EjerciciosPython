from datetime import datetime

def calcular_edad(fecha_nacimiento):
    fecha_actual = datetime.now()
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

def main():
    fecha_nacimiento = input("Por favor ingrese su fecha de nacimiento (YYYY-MM-DD): ")
    try:
        edad = calcular_edad(fecha_nacimiento)
        if edad >= 0:
            print("Usted tiene {} años.".format(edad))
        else:
            print("Fecha de nacimiento inválida.")
    except ValueError:
        print("Formato de fecha incorrecto. Utilice el formato YYYY-MM-DD.")

if __name__ == "__main__":
    main()
