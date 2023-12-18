def filtrar_precios(precios, min, max):
    """
        Funcion que filtra precios dentro de un ranfo
    Args:
        precios (float): Lista de precios
        min (int): valor minimo
        max (int): valor maximo

    Returns:
        Lista: Precios dentro del rango
    """

    en_rango = []
    for precio in precios:
        if precio >= min and precio<= max:
            en_rango.append(precio)
    
    return en_rango

precios = [20.99, 42.33, 55.50, 90.77, 36.77, 47.89, 36, 36]

precios_filtrados = filtrar_precios(precios, 30, 50)
print(precios_filtrados)
print(len(precios_filtrados))