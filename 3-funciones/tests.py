import random

def sumatorio(numeros):
    """
    Funcion que suma todos los elementos de la lista

    Args:
        numeros (list): Lista de numeros
    """
    total = 0 
    for numero in numeros:
        total+= numero
    return total


def suma_lista(numeros):
    return sum(numeros)


# resultado1 = sumatorio([2, 5, 10, 10])
# print(f'Resultado1 {resultado1}')

# resultado2 = sumatorio([100, 200, 300, 400, 500, 600])
# print(f'Resultado2 {resultado2}')

# resultado3 = suma_lista([100, 200, 300, 400, 500, 600])
# print(f'Resultado3 {resultado3}')

# lista1 = [0]
# for i in range(1,7):
#     # print(i*100)
#     lista1.append(i*100)
    
# resultado4 = sumatorio(lista1)
# print(f'Resultado4 {resultado4}')


# lista = [random.randint(100, 600) for i in range(6)]
# print(lista)
# resultado5 = sumatorio(lista)
# print(f'Resultado5 {resultado5}')