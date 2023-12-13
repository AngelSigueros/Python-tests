
hora = int(input('Introduce la hora: '))

if 0 <= hora < 8:
    print('Está durmiendo 😴💤')
elif 8 <= hora < 15:
    print('En clases de Frontend 💻')
elif 15 <= hora < 16:
    print('Comiendo manguito maracatón 🥭')
elif 16 <= hora < 21:
    print('Clase de backend con el míster ❤️')
elif 21 <= hora < 24:
    print('Cenando sano en plan fitness 🐟💪')
else:
    print('Introduce una hora correcta')