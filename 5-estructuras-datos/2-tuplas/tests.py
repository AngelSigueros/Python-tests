Definición de tuplas

Para definir una tupla, se utilizan paréntesis () y se separan los elementos por comas:

tupla_ejemplo = (1, "cadena", 3.14, True)

También es posible definir una tupla sin paréntesis, utilizando solo comas:

tupla_sin_parentesis = 1, "cadena", 3.14, True

Para crear una tupla con un único elemento, es necesario agregar una coma después del elemento (de lo contrario, Python tratará el valor como un tipo de dato no tupla):

tupla_un_elemento = (1,)

Indexación y segmentación (slicing)

Al igual que las listas, se pueden utilizar índices para acceder a los elementos de una tupla:

tupla = (3, 6, 9, 12, 15)

# Acceder al primer elemento
primer_elemento = tupla[0]  # primer_elemento = 3

# Acceder al último elemento
ultimo_elemento = tupla[-1]  # ultimo_elemento = 15

También se puede utilizar el concepto de segmentación o "slicing" para obtener un subconjunto de elementos en una tupla:

tupla = (3, 6, 9, 12, 15)

# Obtener los primeros 3 elementos
primeros_tres = tupla[:3]  # primeros_tres = (3, 6, 9)

# Obtener los elementos del segundo al cuarto (índice 1 al 3)
subconjunto = tupla[1:4]  # subconjunto = (6, 9, 12)

Nótese que para la sementación, el primer índice dado es inclusivo, pero el segundo es exclusivo (tupla[1:4] tomará los elementos del 1 al 3, porque el 4 es exclusivo).
Métodos de las tuplas

A pesar de ser inmutables, las tuplas tienen dos métodos disponibles:

    count(): Retorna el número de veces que aparece un elemento específico en la tupla.

tupla = (1, 2, 3, 2, 1, 2)

# Contar cuántas veces aparece el número 2
cantidad_dos = tupla.count(2)  # cantidad_dos = 3

# Contar cuántas veces aparece el número 5
cantidad_cinco = tupla.count(5)  # cantidad_cinco = 0

    index(): Retorna el índice de la primera aparición de un elemento específico en la tupla. Si el elemento no se encuentra en la tupla, se produce un error (ValueError).

tupla = (1, 2, 3, 2, 1, 2)

# Obtener el índice de la primera aparición del número 3
indice_tres = tupla.index(3)  # indice_tres = 2

# Obtener el índice de la primera aparición del número 2
indice_dos = tupla.index(2)  # indice_dos = 1

Inmutabilidad

Dado que las tuplas son inmutables, no es posible agregar, eliminar o modificar elementos una vez que se crea la tupla. Por ejemplo, el siguiente código arrojará un error:

tupla = (1, 2, 3)
tupla[0] = 5  # Esto causará un TypeError

Sin embargo, se pueden realizar otras operaciones, como concatenar tuplas o repetir una tupla para crear una nueva tupla:

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

# Concatenar dos tuplas
tupla_union = tupla1 + tupla2  # tupla_union = (1, 2, 3, 4, 5, 6)

# Repetir una tupla
tupla_repetida = tupla1 * 3  # tupla_repetida = (1, 2, 3, 1, 2, 3, 1, 2, 3)

En resumen, las tuplas en Python son colecciones ordenadas e inmutables de elementos, que pueden ser de diferentes tipos de datos. Se utilizan principalmente para representar estructuras de datos fijas, donde no se requiere cambiar, agregar o eliminar elementos. Las tuplas cuentan con dos métodos principales: count() e index(), que permiten contar la cantidad de veces que aparece un elemento y obtener el índice de su primera aparición, respectivamente.
Aprendizajes de esta lección

    Comprender qué son las tuplas en Python y cómo se definen.
    Aprender a acceder a los elementos de una tupla utilizando índices y segmentación (slicing).
    Conocer los métodos disponibles para trabajar con tuplas, como count() e index().
    Entender la inmutabilidad de las tuplas y cómo pueden usarse para representar datos fijos o constantes.
    Familiarizarse con operaciones básicas de tuplas, como concatenación y repetición.

