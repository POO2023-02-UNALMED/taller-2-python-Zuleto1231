class Asiento:
    def __init__(self,color , precio ,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    def cambiarColor(self,color):
        if color==("rojo" or "verde" or "amarillo" or "negro" or "blanco"):
            self.color=color
        
        
        
class Auto:
    cantidadCreados=0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
    
    def cantidadAsientos(self):
        return len(self.asientos)
        
    def verificarIntegridad(self):
        originalidad=True
        if self.motor.registro==self.registro:
            for i in range(len(self.asientos)):
                if self.asientos[i].registro!=self.registro:
                    originalidad=False
                    break
        else:
            originalidad=False
        #mensaje de originalidad
        
        if originalidad:
            print("Auto original")
            
        else:
            print("Las piezas no son originales")
        
                    
                    
            
            
            
            
class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
        
    def cambiarRegistro(self,registro):
        self.registro=registro
        
    def asignarTipo(self,tipo):
        if tipo=="electrico" or tipo=="gasolina":
            self.tipo=tipo

if __name__=="__main__":
    motor1=Motor(1,"electrico",1231)
    asiento1=Asiento("amarillo",1000,1231)
    asiento2=Asiento("azul",1000,1231)
    auto1=Auto(2001,2000,[asiento1,asiento2],"Toyota",motor1,1231)
    
    print(auto1.cantidadAsientos())
    
        
    