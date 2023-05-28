numeroif = 20 

if numeroif > 0:
    print('numero positivo')
elif numeroif < 0:
    print("numero negativo")
else:
    print('El numero es cero')

#-----------------------------------------------------
print('inicia while')
numerowhile = 0

while numerowhile < 3:
    print(numerowhile)
    numerowhile += 1
    

#------------------------------------------------------
print('inicia for')
numerofor = 0 

if numerofor <= 3:
    for i in range(4):
        print(i)
        numerofor +=1 

#------------------------------------------------------
print('inicia switch')

estacion = 'primavera'

match estacion:
    case "verano":
        print('es verano, son vacaciones')
    case "primavera":
        print('es primavera, dias calorosos')
    case 'invierno':
        print('es invierno, recuerda llevar sueter')
    case _:
        print('estacion inexistente')
    

