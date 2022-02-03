"""
Para verificar os while's, adicione: print (count), após os dois pontos do while.
Coloquei um import random para caso queira testar vários números dentro do limite estabelecido no desafio. 
Mude a constante de acordo com a preferência para testar se o código está correto. Deixei 
comentado para isto ficar a seu critério.
"""
"""
import random

const = random.randint(-300, 300)
"""
const = -21
count = 0

if const != 0:
    print("Constant", const)

if const == 1:
    print("PLUSONE")

elif const > 0:
    print("PLUSONE")
    count = 1
    while True:
        print(count)
        if count == const:
            break    

        if count*2 > const or count*2 == const:
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
            print(count)

        if count == const:
            break

        if count < const: 
            print ("INC")
            count += 1
    

        if const%2 != 0 and count*2 < const:
            if (count*2) - 1 == const:
                print("DUP")
                count*=2
            if count == const:
                    break
            while (count*2) + 1 != const:
                print("INC")
                count+=1
                if (count*2) + 1 == const:
                    break
                 

        if count == const:
            break
        
        if count*2 < const and const%2 == 0:
            while count != const/2:
                print("INC")
                count+=1
                print(count)
                if count == const/2:
                    break
        


        
        

