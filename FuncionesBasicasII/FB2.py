'''Ejercicio 1: Cuenta regresiva: crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 
Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]'''

import random
#genera un numero random
newvalor=random.randint(5,15)
print("Ejercicio 1: ")
def countdown(entrada):
    lista=[]
    for i in range(entrada,-1,-1):
        lista.append(i)
    return lista

resultado=countdown(newvalor)
print(resultado)

'''Ejercicio 2: Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2'''

print("Ejercicio 2: ")
def imprimir_y_devolver(lista):
    print(lista)
    for num in lista:
        print (num)
        return lista[1]
x=imprimir_y_devolver([9,7])
print(x)

'''Ejercicio 3: Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)'''

print("Ejercicio 3: ")
def primero_mas_longitud(a):
    suma=0
    for i in range(0,len(a)):
        suma=a[i]+len(a)
        return suma
z=primero_mas_longitud([1,2,3,4,5])
print("La suma del 1ero y el largo es: ",z)

'''Ejercicio 4: Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False
Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False'''

print("Ejercicio 4: ")
def valores_mayores_que_el_segundo(mayorque):
    newlista=[]
    cont=0
    if len(mayorque)>1:
        for j in mayorque:
            if j > mayorque[1]:
                newlista.append(j)
                cont+=1
    else:
        return False
    print (cont)
    return newlista
mayores=valores_mayores_que_el_segundo([5,2,3,2,1,4])
print(mayores)
mayores2=valores_mayores_que_el_segundo([3])
print(mayores2)

'''Ejercicio 5: Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]'''

print("Ejercicio 5: ")
def length_and_value(a,b):
    lista=[]
    for i in range(0,a):
        lista.append(b)
    return lista
valor=length_and_value(4,7)
valor2=length_and_value(6,2)
print(valor)
print(valor2)