"""
Para verificar os while's, adicione: print (count), após os dois pontos do while.
Coloquei um import random para caso queira testar vários números dentro do limite estabelecido no desafio. Porém, deixei 
comentado para isto ficar a seu critério.
Mude a constante de acordo com a preferência para testar se o código está correto.
"""
"""
import random

const = random.randint(-32768, 32767)

"""
const = 10
count = 0

if const != 0:
    print("Constant", const)

if const == 1:
    print("PLUSONE")

elif const > 0:
    print("PLUSONE")
    count = 1
    while count != const:
        if count == const:
            break    

        if count*2 > const:
            print("INC")
            count+=1
            if count == const:
                break
        
        if count < const and count*2 < const: 
            print ("DUP")
            count*=2
        
        if count == const:
            break
        


elif const < 0:
    print("MINUSONE")
    count = -1

    while True:
        if count == const:
            break

        if count > const:
            print("DUP")
            count*=2

        if count == const:
            break

        if count < const: 
            print ("INC")
            count += 1

        if count == const:
            break

        

        
        

