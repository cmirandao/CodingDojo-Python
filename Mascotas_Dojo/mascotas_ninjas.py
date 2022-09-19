import mascotas_dojo, ninjas_dojo
premios_pet=["galletitas", "huesitos", "dulces"]
comida_pet=["zanahoria", "tomate", "carne", "pellet"]

dash=mascotas_dojo.Mascota("Dash","perro","hembra negra con blanco",["dar la pata","hablar"],"Guaf Guau")
pay=mascotas_dojo.Mascota("Pay","gato","macho naranja con rayas negras",["ronronear","rodar","jugar con lana"],"miauuuu")
caro=ninjas_dojo.Ninja("Carolina","Miranda",premios_pet,comida_pet,dash)
juan=ninjas_dojo.Ninja("Juan","Perez",premios_pet,comida_pet,pay)

dash.mostrar_info()
print("--------------------------")
pay.mostrar_info()
dash.dormir()
print("--------------------------")
caro.alimentar().caminar().banar()
print("--------------------------")
juan.caminar().alimentar().banar()
print("--------------------------")
dash.mostrar_info()
print("--------------------------")
pay.mostrar_info()