n:int=1

print(f'Grãos contidos nas casas do tabuleiro de xadrez é: {n},',end="")
for i in range(1,64,1):
    n*=2
    print(f'{n},',end='')

