# 1. TAREA: imprime "Hola, mundo"
print("Hola, mundo")
# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Carolina"
print("¡Hola ",name, "!")	# con una coma
print("¡Hola "+name+ "!")	# con un +
# 3. imprimir "Hola 42!" con el número en una variable
age = 36
print("¡Hola ",age, "!")	# con una coma
#print("¡Hola "+name+ "!")	# con una +	-- este debería arrojar un error!
print("¡Hola "+str(age)+ "!")
# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("Amo comer {} y {}".format(fave_food1,fave_food2)) # con .format()
print(f"Amo comer {fave_food1} y {fave_food2}") # con una cadena f

#Bonus
x = "<-- Bonus Ejercicio hola mundo -->"
z = "Los gatos grises tienen 4 gatos naranjos que juegan con 2 gatos negros"
y = "gatos"
print(x.title())
print("Mi nombre es %s y tengo %d años" % (name, age))
print(x.upper())
print(x.lower())
print(z.count(y))
print(x.split())