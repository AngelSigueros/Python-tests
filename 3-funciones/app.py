'''
Menu de opciones
'''
import input_utils as iu
import os

from tests import suma_lista

precios = [2, 5, 10, 10]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_opciones():
    # clear_console()
    print('')
    print('0- Ver precios')
    print('1- Suma precios')
    print('2- Precio por posicion')
    print('3- Nuevo precio')
    print('4- Actualiza precios')
    print('5- Borra un precio')
    print('6- Borrar todos precios')
    print('7- Rango')
    print('8- Salir')
    print('')
    opcion = int(input('Seleccione opcion: '))
    match(opcion):
        case (0):
            ver_precios()
        case (1):
            suma_precios()
        case (2):
            ver_precio_posicion()
        case (3):
            nuevo_precio()
        case (4):
            actualiza_precio()
        case (5):
            borra_precio()
        case (6):
            borra_precios()
        case (7):
            rango_precio()
        case (8):
            salir()    
            return False
        case other:
            print('Opcion no valida')
            clear_console()
            menu_opciones()
    continuar()
    menu_opciones()
    return False

def ver_precios():
    print(precios)
    # clear_console()
    # menu_opciones()

def suma_precios():
    print('Sumando precios')
    suma_precios = suma_lista(precios)
    print(suma_precios)


def ver_precio_posicion():
    print('Sumando precio en posicion')
    pos = iu.read_int('Introduce la posicion: ')
    print(precios[pos])

    
def nuevo_precio():
    print('Nuevo precio')
    precio_new = iu.read_float('Introduce precio: ')
    precios.append(precio_new)


def actualiza_precio():
    print('Actualiza precio')
    precio_new = iu.read_float('Introduce precio a actualizar: ')
    pos = iu.read_int('Introduce la posicion a actualizar: ')
    precios[pos] = precio_new

    
def borra_precio():
    print('Borra precio')
    precio = iu.read_float('Introduce precio a borrar: ')
    print(precios.index(precio))
    precios.remove(precio)

    
def borra_precios():
    print('Borra todos los precios')
    precios.clear()

def rango_precio():
    print('Rango precios')
    rango_min = iu.read_int('Introduce min del rango: ')
    rango_max = iu.read_int('Introduce max del rango: ')
    lista_rango = []
    # for precio in precios:
    #     if precio >= rango_min and precio<= rango_max:
    #         lista_rango.append(precio)
            
    # For en 1 linea
    lista_rango = [precio for precio in precios if rango_min <= precio <= rango_max]
    
    print(lista_rango)

def salir():
    print('Bye!!!')
    return False

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def continuar():
    print('')
    print("Presiona Enter para continuar...")
    input()
    clear_console()
    
menu_opciones()