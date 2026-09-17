n1: int = 0
n2: int = 0
maior: int = 0
result: int = 0
menor: int = 0

n1= int (input ('Insira primeiro valor:'))
n2= int (input ('Insira segundo valor:'))

if(n1>n2):
    maior=n1
    menor=n2
else:
    maior=n2
    menor=n1
result=maior-menor
print('A diferença do valor 1 e 2 é de:', result)



