'''declaración de variables
num1, num2, boolean, string'''
num1 = 42 #tipo de dato número
num2 = 2.3 #tipo de dato número
boolean = True #tipo de dato booleano
string = 'Hello World' #tipo de dato string

#inicialización de lista, valor de acceso
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#inicialización de diccionario
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#inicialización de tupla, valor de acceso
fruit = ('blueberry', 'strawberry', 'banana')

print(type(fruit)) #imprime el tipo de dato de la tupla fruit
print(pizza_toppings[1]) #imprime el valor de la lista pizza_toppings con el indice 1
pizza_toppings.append('Mushrooms') #añadir valor Mushrooms a la lista pizza_toppings
print(person['name']) #imprime el valor que hay en el diccionario en la clave name
person['name'] = 'George' #reasignar valor a la clave name, de John cambia a George
person['eye_color'] = 'blue' #añade al diccionario person la clave eye_color con el valor blue
print(fruit[2]) #imprime el valor que hay en la tupla fruit con el indice 2

'''condicional if
como num1 es 42 no ingresa al if y pasa hasta el else
donde imprime It's lower'''
if num1 > 45: #comienzo del condicional if
    print("It's greater") #fin del condicional if
else: #comienzo del condicional else
    print("It's lower") #fin del condicional else

'''condicional if
con el metodo len obtiene el largo del valor de la variable
string el cual es 11, por lo cual no ingresa al if
ni al elif, solo ingresa al else e imprime Just right!'''
if len(string) < 5: #comienzo del condicional if
    print("It's a short word!") #fin del condicional if, si esta condición se cumpliera imprimiria It's a short word!
elif len(string) > 15: #comienzo del condicional elif
    print("It's a long word!") #fin del condicional elif, si esta condición se cumpliera imprimiria It's a long word!
else: #comienzo del condicional else
    print("Just right!") #fin del condicional else, imprime Just right!

'''bucle for'''
for x in range(5):#comienzo del bucle donde x ira hasta que sea menor a 5 partiendo en 0
    print(x) #imprime el valor de x, incrementa el valor de x en 1, fin del bucle for
for x in range(2,5): #comienzo del bucle donde x ira desde el 2 hasta que sea menor a 5
    print(x) #imprime el valor de x, incrementa el valor de x en 1, fin del bucle for
for x in range(2,10,3): #comienzo del bucle donde x ira desde el 2 hasta que sea menor a 10 declarando que aumentara de 3 en 3
    print(x)#imprime el valor de x, incrementa el valor de x en 3, fin del bucle for

x = 0 #declaración de variable x, inicializandola en 0

'''bucle while
mientras x, partiendo en 0, sea menor a 5'''
while(x < 5): #comienzo del bucle
    print(x) #imprime el valor de x
    x += 1 #incrementa el valor de x en 1, fin del bucle

'''Elimina el último valor de la lista pizza_toppings'''
pizza_toppings.pop()
'''Elimina el valor en el indice 1 de la lista pizza_toppings'''
pizza_toppings.pop(1)
'''Imprime el diccionario person'''
print(person)
'''Elimina la última clave con su valor del diccionario person'''
person.pop('eye_color')
'''Imprime el diccionario person'''
print(person)

'''Bucle for'''
for topping in pizza_toppings: #inicio bucle
    if topping == 'Pepperoni': #inicio condicional if
        '''palabra clave para finalizar el bucle for 
        y continuar con la siguiente iteración, cuando 
        se cumple la condición del if se salta esa iteración'''
        continue 
    print('After 1st if statement')
    if topping == 'Olives': #inicio condicional if
        break #palabra clave para finalizar el bucle

'''Función print_hello_ten_times'''
def print_hello_ten_times(): #inicio de la función, no recibe parámetros
    for num in range(10): #inicio de los argumentos con un bucle for
        print('Hello') #imprime Hello la cantidad de veces indicada en el rango del for

'''Llamada a la función 
esta función no contiene return, solo imprime por consola'''
print_hello_ten_times()

'''Función print_hello_x_times'''
def print_hello_x_times(x): #inicio de la función, recibe 1 parámetro x
    for num in range(x): #inicio de los argumentos con un bucle for que ocupa de rango el parámetro recibido
        print('Hello') #imprime Hello la cantidad de veces indicada en el rango del for

'''Llamada a la función 
esta función no contiene return, solo imprime por consola 4 veces'''
print_hello_x_times(4)

'''Función print_hello_x_or_ten_times'''
#inicio de la función, recibe 1 parámetro x que esta inicializado en 10
# si no recibe uno nuevo toma este valor por defecto
def print_hello_x_or_ten_times(x = 10): 
    for num in range(x): #inicio de los argumentos con un bucle for que ocupa de rango el parámetro recibido
        print('Hello') #imprime Hello la cantidad de veces indicada en el rango del for

'''Llamada a la función 
esta función no contiene return, solo imprime por consola 10 veces (cuando no envia parametros)
y 4 veces (cuando se le envia el número 4). Esto hace que se reasigne el valor del 
parametro x de la función'''
print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

#print(num3) #NameError: el nombre <nombre de la variable> no está definido
num3 = 72
#fruit[0] = 'cranberry' #TypeError: el objeto 'tuple' no admite la asignación de elementos
#print(person['favorite_team']) #KeyError: 'favorite_team', esta clave no existe en el diccionario person
#print(pizza_toppings[7]) #IndexError: índice de lista fuera de rango, la lista solo tiene 4 valores
#   print(boolean) #IndentationError: sangría inesperada
#fruit.append('raspberry') #AttributeError: el objeto 'tuple' no tiene atributo 'append'
#fruit.pop(1) #AttributeError: el objeto 'tuple' no tiene atributo 'pop'