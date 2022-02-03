#Pode ficar a vontade para alterar os elementos da lista em prol de testar
#se o código está funcionando para todos os casos
#por exemplo:
# list_verbs = ["casos", "porre", "corraem", "picel", "param", "piceons", "oficina", "parons"]

list_verbs = ["casos", "porre", "corraem", "picel", "oficina", "param"]

def tense(x):
    if list_verbs[x][-1::] in ["o", "a"] or list_verbs[x][-2::] in ["om", "os","am"]  or list_verbs[x][-3::] in "ons":
        return "present tense" 

    elif  list_verbs[x][-2::] in "ai"  or list_verbs[x][-3::] in ["ais","aem", "aim"]  or list_verbs[x][-1::] in "i"   or list_verbs[x][-4::] in  "aist" :
        return "future tense"

    elif list_verbs[x][-1::] in  "e"   or list_verbs[x][-2::] in ["ei", "es", "em", "im"]  or list_verbs[x][-3::] in  "est":
        return "past tense"

    else:
        return ""


def person(x):
    if list_verbs[x][-1::] in "o" or list_verbs[x][-2::] in ["ei", "ai"]:
        return "1st person"
    elif list_verbs[x][-2::] in ["os", "es"]  or list_verbs[x][-3::] in "ais": 
        return "2nd person"
    elif list_verbs[x][-1::] in ["a", "e", "i"]:
        return "3rd person"
    elif list_verbs[x][-2::] in ["om", "em"] or  list_verbs[x][-3::] in "aem":
        return "4th person"
    elif list_verbs[x][-3::] in ["ons", "est"]  or list_verbs[x][-4::] in "aist":
        return "5th person"
    elif list_verbs[x][-2::] in ["am", "im"] or list_verbs[x][-3::] in "aim" :
        return "6th person"
    else:
        return ""

for x in range(len(list_verbs)):
    print("-"*10, x, list_verbs[x], "-"*10)
    if list_verbs[x][-1::] in ["o", "a", "e", "i"]:
        print("verb", list_verbs[x][:-1]+"en")
    elif list_verbs[x][-3::] in ["ons", "est", "ais", "aem", "aim"] :
        print("verb", list_verbs[x][:-3]+"en")
    elif list_verbs[x][-2::] in ["om", "os", "am", "ei", "es", "em", "im", "ai"] :
        print("verb", list_verbs[x][:-2]+"en")
    elif  list_verbs[x][-4::] in "aist":
        print("verb", list_verbs[x][:-4]+"en")
    else:
        print("not a verb case")
    print(tense(x))
    print(person(x))
    



  
