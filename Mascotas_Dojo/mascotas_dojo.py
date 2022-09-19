import random, tipo_mascotas
class Mascota(tipo_mascotas.TipoMascota):
    def __init__(self, nombre, tipo, desc, trucos, ruidos):
        super().__init__(tipo, desc)
        self.nombre = nombre
        self.trucos = trucos
        self.salud = 100
        self.energia = 50
        self.ruidos = ruidos
    
    def mostrar_info(self):
        super().mostrar_info(self.nombre)
        print(f"nivel de salud: {self.salud}, nivel de energía: {self.energia}")
        return self
        
# implementa los siguientes métodos:
# dormir() - incrementa la energía de la mascota en 25
    def dormir(self):
        self.energia+=20
        print(f"{self.nombre} esta durmiendo")
        return self
# comer() - incrementa la energía de la mascota en 5 y la salud en 10
    def comer(self):
        self.energia+=10
        self.salud+=20
        print("Ñam Ñam")
        return self
# jugar() - incrementa la salud de la mascota en 5
    def jugar(self):
        self.energia-=20
        self.salud+=5
        #genera un numero random
        newvalor=random.randint(0,len(self.trucos)-1)
        print(f"{self.nombre} puede {self.trucos[newvalor]}")
        return self
# ruido() - imprime el sonido que produce la mascota
    def ruido(self):
        print(f"{self.ruidos}")
        return self