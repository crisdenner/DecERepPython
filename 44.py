base:int=0
exp:int=0
pot:int=0
potrep:int=1

base=int(input("insira a base: "))
exp=int(input("insira o expoente: "))

pot=base**exp
print(f'potencial com python: {pot}')

for i in range (1,exp+1,1):
    potrep=potrep*base
print(f"potencial com repetição: {potrep}")



