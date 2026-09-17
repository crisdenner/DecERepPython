n1: int = 0
n2: int = 0
n3: int = 0
n4: int = 0
media: int = 0

n1= int(input('Insira primeira nota:'))
n2= int(input('Insira segunda nota:'))
n3= int(input('Insira terceira nota:'))
n4= int(input('Insira quarta nota:'))

media= int(n1+n2+n3+n4)/4
if(media>6):
    print('APROVADO')
elif(media<6 and media>=3):
    print('EXAME')
else:
    print('REPROVADO')


