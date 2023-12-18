import tests as t1

from test3 import filtrar_precios
from test2 import contar_vocales_2

precios = [20.99, 42.33, 55.50, 90.77, 36.77, 47.89, 36, 36]

# precios_filtrados = test3.filtrar_precios(precios, 30, 50)
precios_filtrados = filtrar_precios(precios, 30, 50)

resultado1= contar_vocales_2('Alän')

resultado3 = t1.suma_lista([100, 200, 300, 400, 500, 600])

