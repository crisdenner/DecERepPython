cont:int = 1
fat:float =1.0
n:int=0
ac:float=0.0
total: float=1.0



n=float(input('Insira o valor: '))


while cont<=n:
    fat *= cont
    ac = 1/fat
    print(f"O resultado de 1/{fat} é: {ac}")
    total += ac
    cont+=1
print(f'O total da soma é: {total}')




