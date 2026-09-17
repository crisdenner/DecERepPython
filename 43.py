ana:float=1.1
maria:float=1.5
anos:int=0

while(ana<maria):
    ana+=0.03
    maria+=0.02

    anos+=1
print(f"Ana levara {anos} anos para alcançar Maria. Ana com {ana:.2f}Mt e Maria com {maria:.2f}Mt")
