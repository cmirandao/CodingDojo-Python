import random
class Ninja:
    def __init__(self, nombre, apellido, premios, comida_mascota, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.premios = premios
        self.comida_mascota = comida_mascota
        self.mascota = mascota
# implementa los siguientes métodos:
# caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()
    def caminar(self):
        self.mascota.jugar()
        newpremio=random.randint(0,len(self.premios)-1)
        print(f"Asi que se gano {self.premios[newpremio]} y esta paseando")
        return self
# alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()
    def alimentar(self):
        if len(self.comida_mascota) > 0:
            comida=self.comida_mascota.pop()
            print(f"{self.nombre} esta alimentando a {self.mascota.nombre} con {comida}")
            self.mascota.comer()
        else:
            print("Necesitas más comida para tú mascota")
        return self
# bañar(): limpia la mascota del ninja invocando el método de mascota sonido()
    def banar(self):
        print(f"{self.mascota.nombre} se esta bañando")
        self.mascota.ruido()