nominados = ["Alba 2", "Antoni 4", "Aroa 5", "Dani 8", "Juan 10"]

aprbados=0
suspensos=0

for nota in nominados:
    # valor=int(nota.split()[1])
    if int(nota.split()[1]) >= 5:
        aprbados+=1
    else:
        suspensos+=1
        
print('Aprobados: ', aprbados)
print('Suspensos: ', suspensos)