voltas:int = 0
metros:int = 0
minutos:int = 0
kms:int = 0
horas:int = 0
kmh:int=0

voltas=int(input('Insira as voltas:'))
metros=int(input('Insira quantos metros tem o circuito:'))
minutos=int(input('Insira quantos minutos no total:'))

kms=(voltas*metros)/1000
horas=(minutos/60)
kmh= kms/horas
print('A media de velocidade foi: ',kmh)


