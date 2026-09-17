cont:int=0

n=int(input('Insira o resultado dos dados para ver quantas possibilidades de dar esse valor: '))
for d1 in range(1,7):
    for d2 in range(1,7):
        if d1+d2 == n:
            cont+=1
print(f"A quantidade de possibilidades de 2 dados dar igual a {n} é: {cont}")

