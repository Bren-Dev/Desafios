list_verbs = ["casos", "porre", "corraem", "picel", "oficina", "param"]

def tense():
    if "o" in list_verbs[x][-1::] or "a" in list_verbs[x][-1::] or "om" in list_verbs[x][-2::] or  "os" in list_verbs[x][-2::] or  "am" in list_verbs[x][-2::] or "ons" in list_verbs[x][-3::]:
        return "present tense" 

    elif "ai" in list_verbs[x][-2::] or "ais" in list_verbs[x][-3::] or "i" in list_verbs[x][-1::] or "aem" in list_verbs[x][-3::] or "aist" in list_verbs[x][-4::] or "aim" in list_verbs[x][-3::]:
        return "future tense"

    elif "e" in list_verbs[x][-1::]  or "ei" in list_verbs[x][-2::] or "es" in list_verbs[x][-2::] or "em" in list_verbs[x][-2::]  or "im" in list_verbs[x][-2::] or "est" in list_verbs[x][-3::]:
        return "past tense"

    else:
        return ""


def person():
    if "o" in list_verbs[x][-1::] or "ei" in list_verbs[x][-2::] or "ai" in list_verbs[x][-2::]:
        return "1st person"
    elif "os" in list_verbs[x][-2::] or "es" in list_verbs[x][-2::] or "ais" in list_verbs[x][-3::]: 
        return "2nd person"
    elif "a" in list_verbs[x][-1::] or "e" in list_verbs[x][-1::] or "i" in list_verbs[x][-1::]:
        return "3rd person"
    elif "om" in list_verbs[x][-2::] or "em" in list_verbs[x][-2::]  or "aem" in list_verbs[x][-3::]:
        return "4th person"
    elif "ons" in list_verbs[x][-3::] or "est" in list_verbs[x][-3::] or "aist" in list_verbs[x][-4::]:
        return "5th person"
    elif "am" in list_verbs[x][-2::] or "im" in list_verbs[x][-2::] or "aim" in list_verbs[x][-3::]:
        return "6th person"
    else:
        return ""

for x in range(len(list_verbs)):
    print("-"*10, x, list_verbs[x], "-"*10)
    if  "o" in list_verbs[x][-1::] or "a" in list_verbs[x][-1::] or "e" in list_verbs[x][-1::] or "i" in list_verbs[x][-1::]:
        print("verb", list_verbs[x][:-1]+"en")
    elif "ons" in list_verbs[x][-3::] or "est" in list_verbs[x][-3::] or "ais" in list_verbs[x][-3::] or  "aem" in list_verbs[x][-3::] or "aim" in list_verbs[x][-3::]:
        print("verb", list_verbs[x][:-3]+"en")
    elif "om" in list_verbs[x][-2::] or  "os" in list_verbs[x][-2::] or  "am" in list_verbs[x][-2::] or "ei" in list_verbs[x][-2::] or "es" in list_verbs[x][-2::] or "em" in list_verbs[x][-2::] or "im" in list_verbs[x][-2::] or "ai" in list_verbs[x][-2::]:
        print("verb", list_verbs[x][:-2]+"en")
    elif "aist" in list_verbs[x][-4::]:
        print("verb", list_verbs[x][:-4]+"en")
    else:
        print("not a verb case")
    print(tense())
    print(person())
    



  
