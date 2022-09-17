# #1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
'''devuelve un 5'''

#2
def number_of_military_branches():
    return 5
#solo para argumentar respuesta se define metodo faltante
def number_of_days_in_a_week_silicon_or_triangle_sides():
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
'''
el metodo number_of_days_in_a_week_silicon_or_triangle_sides() no esta definido por lo cual arrojara un error,
primero se debe definir el metodo para que funcione
'''

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
'''retornara un 5 ya que al ejecutar linea por linea entra en el primer return y se sale del metodo porque return detiene la función por lo cual no envia la siguiente linea'''

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
'''al igual que el ejemplo 3 solo retorna el 5 y detiene la función'''

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
'''la variable x guarda lo que contiene el metodo number_of_great_lakes() y en la siguiente linea se imprime. Como el metodo no retorna nada el interprete de python devuelve "None" y que espera un valor de retorno'''

#6
def add(b,c):
    print(b+c)
    return b+c
#Solo para argumentar respuesta se muestran formas de corregir el error
print(add(1,2) , add(2,3))
print(add(1,2) + add(2,3))
'''el print de la 3era linea llama 2 veces al metodo add, en la 1era obtiene el número 3 y el segundo el número 5 pero no se puede ocupar el operador + ya que no esta devolviendo nada el metodo y no puede sumar los números recibidos, solo imprime . Si se cambiara por "," imprimiria 3, 5, None, None que son los valores que entrega el metodo con los parametros entregados y ademas indica que no devuelven nada. Si se agregara un return b+c y se mantuviera el operador + en el print mostraria por consola: 3, 5, 8. En este mismo caso pero cambiando por "," en el print muestra: 3,5,3 5'''


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
'''imprime 25 ya que str convierte el numero a string y el operador + los concatena'''


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
'''al llamar el metodo imprime 100, 10 y no devuelve 7 ya que el metodo termina cuando termina el ciclo else'''


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
'''se imprime lo siguiente:
7
14
21
A diferencia del ejercicio 6 el operador + en este caso opera como suma ya que el metodo devuelve un número'''


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
'''imprime 8, en el primer return termina el metodo'''

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
'''La consola muestra:
500
500
300
500
b=300 solo se ocupa dentro del metodo'''

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
'''La consola muestra:
500
500
300
500
como no hay ninguna variable que reciba el return, este no se muestra'''

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
'''La consola muestra:
500
500
300
300
En este caso una variable fuera del metodo recibe el return del mismo y por eso se muestra'''

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
'''La consola muestra:
1
3
2'''

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
'''La consola muestra:
1
3
5
10'''