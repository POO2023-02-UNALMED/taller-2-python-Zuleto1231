class Asiento:
    def __init__(self,color , precio ,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    def cambiarColor(self,color):
        if color in ("rojo" , "verde" , "amarillo" , "negro" , "blanco"):
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
        cantidad=0
        for i in range(len(self.asientos)):
            if self.asientos[i]!=None:
                cantidad+=1
            
        return cantidad
        
    def verificarIntegridad(self):
        originalidad=True
        if self.motor.registro==self.registro:
            for i in range(len(self.asientos)):
                if self.asientos[i]!=None:
                    if self.asientos[i].registro!=self.registro:
                        originalidad=False
                        break
        else:
            originalidad=False
        #mensaje de originalidad
        
        if originalidad:
            return "Auto original"
            
        else:
            return "Las piezas no son originales"
        
                    
                    
            
            
            
            
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


        
    