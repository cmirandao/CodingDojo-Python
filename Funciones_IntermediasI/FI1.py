# '''1-Actualizar valores en diccionarios y listas:
# Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
# Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
# En el directorio_deportes, cambia "Messi" por "Andrés".
# Cambia el valor 20 en z a 30.'''
print("Ejercicio 1 --->")
x = [ [5,2,3], [10,8,9] ] 
print("lista: ",x)
x[1][0]=15
print("nueva: ",x)

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print("Original: ",estudiantes)
estudiantes[0]["last_name"]="Bryant"
print("Cambio: ",estudiantes)

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
print("Original: ",directorio_deportes)
directorio_deportes['fútbol'][0]="Andrés"
print("Cambio: ",directorio_deportes)

z = [ {'x': 10, 'y': 20} ]
print("Original: ",z)
z[0]["y"]=30
print("Cambio: ",z)

'''2-Iterar a través de una lista de diccionarios:
Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:'''
print("\nEjercicio 2 --->")
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(estudiantes):

    for i in estudiantes:
        for j, a in i.items():
            print(f"{j} - {a}, ",end='')
        print("")
iterateDictionary(estudiantes)
# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

'''3-Obtener valores de una lista de diccionarios
Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:
Michael
John
Mark
KB
Y iterateDictionary2('last_name', estudiantes) debería generar:
Jordan
Rosales
Guillen
Tonel
'''
print("\nEjercicio 3 --->")
def iterateDictionary2(key_name, some_list):
    for i in estudiantes:
        for j, a in i.items():
            if j==key_name:
                print(a)

iterateDictionary2("first_name", estudiantes)
print("\n")
iterateDictionary2("last_name", estudiantes)

'''4-Iterar a través de un diccionarios con valores de lista:
Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:
7 UBICACIONES
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORES
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon'''
print("\nEjercicio 4 --->")
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for i in some_dict:
        print("--------------------")
        print(len(some_dict[i])," ",i.upper())
        for j in range(len(some_dict[i])):
            print(some_dict[i][j])
printInfo(dojo)