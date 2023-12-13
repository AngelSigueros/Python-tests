
# Crear lista

lista_vacia = []
lista_numeros = [1, 2, 3, 4, 5]
lista_mixta = [1, "dos", 3.0, [4, 5]]
lista = [0, 1, 2, 3, 4]
students = ['Aitor', 'Angel', 'Angel 2', "Pepe"]

print(students)
print(lista)
# print(students[4]) IndexError: list index out of range
primer_elemento = lista[0] # 0
segundo_elemento = lista[1] # 1
ultimo_elemento = lista[-1] # 4
penultimo_elemento = lista[-2] # 3

try:
    print(students[0])
    print(students[1])
    print(students[2])
    print(students[3])
    print(ultimo_elemento)
    print(penultimo_elemento)
    print(lista[3])
except IndexError:
    print("Se produjo un IndexError: el índice está fuera del rango de la lista.")


