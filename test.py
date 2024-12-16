def cml():
    hmotnostvstup = input("Zadej hmotnost ")
    try:
        hmotnost = float(hmotnostvstup)
    except ValueError:
        print("Musíš zadat číslo")
        return
    bmr = hmotnost*24.2
    cml = bmr*1.5
    round(cml, 2)
    print(cml)
cml()

from random import randint
from random import randrange
def SQUATCHALLENGE():
    print("V této výzvě musíš každý den udělat tolik dřepů, kolik ti zde padne !")
    print("Jsi ready na dnešek? Určitě!")

    number1 = str(randint(1,10))
    number2 = str(randrange(20,100,10))
    print("Musíš HNED udělat "+number1+" dřepů! Tak rychle!")
    print("Musíš DNES ještě udělat "+number2+" dřepů!")
    print("Pokud máš splněno tak dobrá práce!")

SQUATCHALLENGE()


print("Jakého jsi pohlaví?")
user = input()
if user == "muž" :
    reference = "Vážený pane"
elif user == "žena":
    reference = "Vážená ženo"
else:
    reference = "něco jiného"
print("Vítej " + reference)

