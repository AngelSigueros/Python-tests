# Ejemplo 1: si dentro de una función se cambia el valor de una variable, fuera no tiene efecto:

def method1(param):
    print(param)
    param = 10
    print(param)


number = 5
method1(number)
print(number)
print("===============================")

# Ejemplo 2: para que tenga efecto, se declara fuera y se utiliza
# la palabra reservada global dentro de la función
number2 = 20


def method2():
    global number2
    print(number2)
    number2 = 3
    print(number2)


method2()
print(number2)
