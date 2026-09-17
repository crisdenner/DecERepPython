cont:int =0
fat:int =0

fat=int(input('Insira o valor a ser fatorado:' ))
cont= fat-1
while cont!=0:
    fat=fat*cont
    cont=cont-1
print(f'O resultado é:{fat}')    

