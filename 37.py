cont: int =3
ant: int=1
pos: int=0
atual: int=1
n: int=0

n=int(input('Até qual numero de fibonnacci voce gostaria de ver: '))
print(f"{ant},{atual},",end="")

while(cont<=n):
    pos= ant+atual
    print(f"{pos},",end="")
    ant=atual
    atual=pos
    cont+=1





