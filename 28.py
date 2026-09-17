preco:float = 0.0
vendas:int = 0

preco=float(input('Insira o preço atual  do produto:'))
vendas= int(input('Insira as vendas mensais do produto:'))

if(vendas<500 and preco<30.0):
    preco=preco+(preco*0.1)
    print('Novo preço é: ',preco)
elif(vendas>=500 and vendas<1000 and preco>=30.0 and preco<80.0):
    preco=preco+(preco*0.15)
    print('Novo preço é: ',preco)
elif(vendas>=1000 and preco>=80.0):
    preco=preco-(preco*0.05)
    print('Novo preço é: ',preco)
else:
    print('O preço deve se manter igual')

