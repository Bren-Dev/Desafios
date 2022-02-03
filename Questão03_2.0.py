#Eu criei este segundo arquivo para a questão 3 porque fiquei em dúvida se alterava manualmente
#ou deixava o usuário ir escolhendo as constantes à vontade. 
#no caso, este é o arquivo no qual o usuário escolhe as constantes à vontade

def plusone():
    print("PLUSONE")
    count = 1
    while True:
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

def minusone():
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

        if count*2 < const and const%2 == 0:
            while count != const/2:
                print("INC")
                count+=1
                if count == const/2:
                    break

while True:
    const = int(input("Insira a constante: "))
    count = 0
    while const != 0:
        print("Constant", const)
        break
    if const == 0:
        print("Programa finalizado!")
        break
    if const == 1:
        print("PLUSONE")
    if const == 2:
        print("PLUSONE")
        print("DUP")
    while const > 2:
        plusone()
        break
    while const < 0: 
        minusone()
        break