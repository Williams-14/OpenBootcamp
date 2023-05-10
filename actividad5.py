Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.



def bisiesto(año):
    if año % 4 ==0:
        print(f"{año} es bisiesto")
    else:
        print(f"{año} no es bisiesto")
  
num = int(input("Ingrese un año por favor:\n"))
bisiesto(num)
