#Mu Online
#Clase principal del personaje
class pj:
    
    def __init__(self, nombredelpersonaje, raza,fue,agi,ene,mapa):
        # stats
        self.nombredelpersonaje = nombredelpersonaje
        self.raza = raza
        self.fuerza = fue
        self.agility = agi
        self.energia = ene
        self.mapa = mapa
        
#Nombre de personaje
print('Creador de personaje')
nombredelpj = str(input('Nombre de Personaje: '))


#Raza de personaje
print(' 1-BK \n', '2-Elf\n', '3-SM\n', '4-MG\n')
razaaelegir = int(input('Elegir Raza: '))
if razaaelegir == 1:
    razainicial = 'BK'
elif razaaelegir == 2:
    razainicial = 'Elf'
elif razaaelegir == 3:
    razainicial = 'SM'
elif razaaelegir == 4:
    razainicial = 'MG'

#Que estadistica deseas subir
print(' 1-Lorencia \n', '2-Noria\n', '3-Devias\n')
opcion = int(input('Mapa de inicio: '))
if opcion == 1:
    mapa = 'Lorencia'
elif opcion == 2:
    mapa = 'Noria'
elif opcion == 2:
    mapa = 'Devias'

#Cuantos puntos deseas subir en fuerza?
print('Cuantos puntos deseas subir en fuerza?\n')
fuerza = int(input('Cantidad de puntos en fuerza: '))

#Cuantos puntos deseas subir en agilidad?
print('Cuantos puntos deseas subir en agilidad?\n')
agilidad = int(input('Cantidad de puntos en agilidad: '))

#Cuantos puntos deseas subir en energia?
print('Cuantos puntos deseas subir en energia?\n')
energia = int(input('Cantidad de puntos en energia: '))


#Creacion del personaje
pj1 = pj(nombredelpj,razainicial,fuerza,agilidad,energia,mapa)

print(f"'Su {pj1.raza} fue creado con exito,su mapa inicial es {pj1.mapa}'\nStats\n Fuerza: {pj1.fuerza}\n Energia: {pj1.energia}\n Agilidad: {pj1.agility}   ")
##################################################################################




