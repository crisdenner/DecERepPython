tipo: int = 0
invest: float = 0.0

tipo= int(input('Insira o tipo de conta(sendo 1 Conta Poupança. 2 Renda Fixa):'))
invest= float(input('Insira o valor investido:'))

if(tipo==1):
    invest=invest+(invest*0.03)
    print('O valor corrigido com rendimento de 30 dias na sua Conta Poupança é:',invest)
elif(tipo==2):
    invest=invest+(invest*0.05)
    print('O valor corrigido com rendimento de 30 dias na sua Conta Renda Fixa é:',invest)
else:
    print('Tipo de conta Inválido')
    