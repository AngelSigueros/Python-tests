
# El ámbito de vida de una variable creada dentro de una función es solamente dentro de esa función
# fuera no existirá

def saludo():
    mensaje = "Hola!"
    print(mensaje)


saludo()

# Da error porque la variable mensaje está en el scope de la función y no fuera.
# print(mensaje)