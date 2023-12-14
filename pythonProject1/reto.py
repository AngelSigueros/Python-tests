# Condicional if
numero = 10
if numero > 0:
    print("El número es positivo.")

# Condicional else
numero = -10
if numero > 0:
    print("El número es positivo.")
else:
    print("El número no es positivo.")

# Condicional elif
numero = 0
if numero > 0:
    print("El número es positivo.")
elif numero == 0:
    print("El número es cero.")
else:
    print("El número no es positivo.")

# Bucle for
for i in range(1, 11):
    print(i)

# Bucle while
i = 1
while i <= 10:
    print(i)
    i += 1

# Sentencia break
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# Sentencia continue
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Sentencia pass
for i in range(1, 11):
    pass  # Aquí irá el código en el futuro

