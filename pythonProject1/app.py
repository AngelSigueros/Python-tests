print('PyThon!')
# print('PyThon!')

"""
comentario
"""

# dsfsdf
# dsfgdsfds
# dsgfdsg
# fdgdfgsg

# strip() elimina los espacios en blanco al principio y al final de una cadena
s = "   Hola Mundo!   "
print(s.strip())  # Salida: "Hola Mundo!"

# lower() convierte todos los caracteres de una cadena a minúsculas
s = "HOLA MUNDO!"
print(s.lower())  # Salida: "hola mundo!"

# upper() convierte todos los caracteres de una cadena a mayúsculas
s = "hola mundo!"
print(s.upper())  # Salida: "HOLA MUNDO!"

# replace() reemplaza una subcadena en una cadena por otra subcadena
s = "Hola mundo!"
print(s.replace("mundo", "Python"))  # Salida: "Hola Python!"

# split() divide una cadena en una lista donde cada palabra es un elemento de la lista
s = "Hola mundo!"
print(s.split())  # Salida: ['Hola', 'mundo!']

# format() formatea una cadena utilizando variables
nombre = "Python"
mensaje = "Hola, {}!"
print(mensaje.format(nombre))  # Salida: "Hola, Python!"

regalos = 123
alumnos = 25

regalos_persona = regalos // alumnos
print(f'regalos por persona {regalos_persona}')
print(f'regalos por persona {regalos // alumnos}')

password = input('introduce contraseña: ')
password_correct = 'admin'
print(password == password_correct)

email = input('introduce Email: ').lower()
print(email)
email_correct = 'a@a.a'
print(email_correct)
print(email == email_correct)
print(email!=email_correct)

# if password!=password_correct:
#     print('OK?', password!=password_correct)

print('OK?', password!=password_correct)
print('OK?', password==password_correct)

print(email)
print(password)
print(email_correct)
print(password_correct)
print('Pasas? ', password==password_correct and email==email_correct)