
vehis=['c1', 'c2', 'c3', 'c4']

for coche in vehis:
    if coche.endswith('3'):
        continue
    print(coche)
    
password = 'admin'
password_user = ''

while password_user != password:
    password_user = input('Introduce tu contraseña: ')


print('fin')

intento=1
max_intentos=3
while intento<=3:
    password_user = input('Introduce tu contraseña: ')
    if password_user == password:
        print('Correcto!')
        break
    intento+=1
    
if intento>3:
    print('Numero max de intentos. Sorry!')
    
print('fin')
