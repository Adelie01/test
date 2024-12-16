from random import randint
from random import randrange

def cml():
    hmotnostvstup = string("Kolik vážíš? ")
    try:
        hmotnost = float(hmotnostvstup)
    except ValueError:
        print("Zadejte číslo.")
        return
    bmr = hmotnost*24.2
    cml = bmr*1.5
    round(cml, 2)
    print(cml)
cml()

def SQUATCHALLENGE():
    print("Musíš udělat tolik dřepů, jaké číslo ti padne.")
    print("Ready?")

    number1 = str(randint(1,10))
    number2 = str(randrange(20,100,10))
    print("Teď udělej "+number1+" dřepů! Hurá do toho!")
    print("Ještě dneska udělej "+number2+" dřepů!")
    print("Hotovo? Gut job!!")

    
#SQUATCHALLENGE()
# shift + "

print("Tvoje pohlaví je? - žena/muž")
sex_invalid = True
sex = input()
while sex_invalid:
    if sex == "muž":
        reference = "Vážený sire"
        sex_invalid = False
    elif sex == "žena":
        print("Chcete být oslovována jako lady nebo mademoiselle?")
        selection = input()
        if selection == "lady":
            reference = "Vážená lady"
        elif selection == "mademoiselle":
            reference = "Vážená mademoiselle"
        else:
            print("Nevybrala jste si, jste tedy ženská")
            reference = "Vážená ženská"
        sex_invalid = False
    else:
        print("Tvoje pohlaví je? - žena/muž")
        sex = input()
print("Vítejte " +reference)
