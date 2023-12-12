# Las funciones pueden recibir parámetros y utilizarlos en su interior como si fueran variables.

def hola1():
    print('Hola')


def hola2(name):
    print('Hola {}'.format(name))


def hola3(name='Ricardo'):
    print('Hola {}'.format(name))


def hola4():
    """
    Not yet implemented
    """
    pass


def hola5():
    return 'Hola mundo'


def create_product(id_product, name, color, height, width, weight, price, manufacturer):
    print('text')


# Invocar funciones
hola1()
hola2('Alan')
hola3()
hola3('Juan')
hola4()
print(hola5())
create_product(1, '', 'black', 30, 21, 45, 5.00, 'Samsung')