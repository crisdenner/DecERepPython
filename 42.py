soma:int=0
den:int=0
print('Calculo serie: ',end="")
for num in range(1,51,1): 
    if num==1:
        soma=1
    else:
        den=num+num-1
        soma+=num/den
    print(f'{num}/{den} + ',end='')
print(f" = {soma}")
    



        

