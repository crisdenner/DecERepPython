n:int =0
mn:int =1
ma:int =1

for i in range(1,101):
    while True: 
        n=int(input(f'Insira o valor o n{i}:'))
        if n>0:
            break
        print('Numero invalido')
    if(i == 1):
        ma=n
        mn=n
    else:
        if(n>ma):
            ma=n
        if(n<mn):
            mn=n
print(f'O maior numero foi: {ma} e  o menor numero foi {mn}')