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

class TipoMascota():
    def __init__(self, tipo, desc):
        self.tipo=tipo
        self.desc=desc
    def mostrar_info(self, nombre):
        
        print(f"{nombre} Tipo de mascota: {self.tipo}, descripción: {self.desc}")

class Mascota(TipoMascota):
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

premios_pet=["galletitas", "huesitos", "dulces"]
comida_pet=["zanahoria", "tomate", "carne", "pellet"]

dash=Mascota("Dash","perro","hembra negra con blanco",["dar la pata","hablar"],"Guaf Guau")
pay=Mascota("Pay","gato","macho naranja con rayas negras",["ronronear","rodar","jugar con lana"],"miauuuu")
caro=Ninja("Carolina","Miranda",premios_pet,comida_pet,dash)
juan=Ninja("Juan","Perez",premios_pet,comida_pet,pay)

dash.mostrar_info()
print("--------------------------")
caro.alimentar().caminar().banar()
print("--------------------------")
juan.caminar().alimentar().banar()
print("--------------------------")
dash.mostrar_info()