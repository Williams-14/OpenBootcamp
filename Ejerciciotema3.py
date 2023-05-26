def suma(a,b,c):
    operacion = a + b + c
    return operacion
    
print(suma(2,4,5))
print("Aqui termina la función suma")

#inicio de la creación de la clase coche

class coche:
    def __init__(self, puertas, color):
    
        self.puertas = puertas
        self.color = color
    
    def miCoche(self):
        print("puertas", self.puertas)
        print("color:", self.color)
        
        
        
auto = coche(4, "azul")
auto.miCoche()
        
        
        