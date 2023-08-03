'''
num1 = int(input("primo numero? "))
num2 = int(input("secondo numero? "))
num3 = int(input("terzo numero? "))
if (num1>=num2 and num1>=num3):
    print("Il primo numero "+str(num1)+" è il più grande. La somma dei numeri è:"+str(num1+num2+num3))
elif (num2>=num3):
    print("Il secondo numero "+str(num2)+" è il più grande. Il prodotto dei numeri è:"+str(num1*num2*num3))
else: 
    print("Il terzo numero " + str(num3)+ " è il più grande")
'''
from funzione import sommaNumeri,sottraiNumeri,moltiplicaNumeri,dividiNumeri

while 1:
    num1 = int(input("primo numero? "))
    num2 = int(input("secondo numero? "))
    oper = input("quale operazione vuoi (+,-,*,/)? ")
    if (oper=='+'):
         print(sommaNumeri(num1,num2))
    elif (oper=='-'):
         print(sottraiNumeri(num1,num2))
    elif (oper=='*'):
         print(moltiplicaNumeri(num1,num2))
    else:
         print(dividiNumeri(num1,num2))
    scelta = input("chiudere la calcolatrice? ")
    if (scelta=="si"):
        break