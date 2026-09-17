mult: int=0
n: int=0


n=int(input('Insira o valor para a tabuada: '))

for i in range(1,11):
    mult=n*i
    print(f'{n}x{i} é: {mult}')


