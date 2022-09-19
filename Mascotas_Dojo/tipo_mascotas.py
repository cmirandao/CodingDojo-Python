class TipoMascota():
    def __init__(self, tipo, desc):
        self.tipo=tipo
        self.desc=desc
    def mostrar_info(self, nombre):
        
        print(f"Mascota: {nombre}, tipo: {self.tipo}, descripción: {self.desc}")