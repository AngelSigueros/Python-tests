
# La palabra reserva pass permite crear una función sin tener que añadir el código
# Se utiliza cuando se está empezando a crear un programa y se postpone la implementación
# de una función para más adelante


def retrieve():
    """
    Esto es un comentario multilínea.
    Recupera listado de productos de la base de datos
    """
    pass


def create(product):
    """
    Inserta un producto en base de datos
    """
    pass


def update(product):
    """
    Actualiza un producto
    """
    pass


def delete(id_product):
    """
    Borra un producto
    """
    pass


# Invocar funciones
retrieve()

product_db = 'Mesa'
delete(product_db)
