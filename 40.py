n1: int=0
n2: int=0

n1=int(input('Insira o primeiro numero: '))
n2=int(input('Insira o segundo numero:'))

print(f'Numeros primos entre {n1} e {n2}: ',end='')

for num in range(n1,n2+1,1):

    contprim =0

    for i in range(1,num+1,1):
        if num%i == 0:
            contprim+=1

    if(contprim==2):
        print(f"{num},",end='')



