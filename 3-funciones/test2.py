def contar_vocales(texto):
    """
        Funcion que suma las vocales de un texto
    Args:
        texto (string): Texto para contar las vocales
    """
    total=0
    vocales = ['a', 'e', 'i', 'o', 'u']
    for c in texto:
        if c.lower() in vocales: # c in 'aeiouAEIOUáéíóúÁÉÍÓÚäëïöüÄËÏÖÜ'
            total+=1
    return total

def contar_vocales_2(texto):
    """
        Funcion que suma las vocales de un texto
    Args:
        texto (string): Texto para contar las vocales
    """
    total=0
    vocales = ['a', 'e', 'i', 'o', 'u']
    for c in texto:
        if c in 'aeiouAEIOUáéíóúÁÉÍÓÚäëïöüÄËÏÖÜ':
            total+=1
    return total

resultado1= contar_vocales('Alän')
print(f'Resultado1 {resultado1}')

resultado2 = contar_vocales_2('Holá mUndO')
print(f'Resultado2 {resultado2}')