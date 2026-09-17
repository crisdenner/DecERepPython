calc:int=0
den:int=0
print('Calculo serie: ',end="")
for num in range(1,16,1): 
    den=num*num
    if num%2==0:
        calc-=num/den
        print(f'{num}/{den} + ',end='')
    else:
        calc+=num/den
        print(f'{num}/{den} - ',end='')


 
print(f" = {calc:.2f}")