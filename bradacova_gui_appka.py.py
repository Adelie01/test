from tkinter import *
from bradacova_lekce6_appka import *

#funkce volané tlačítky
def set_jmeno():
    odpoved = "" + jmeno.get()
    info_jmeno["text"] = odpoved

def set_vyzva():
    info_jmeno["text"] = now_squat_challenge()

#okno aplikace
okno = Tk()
okno.title("FIT-NESS")
okno.geometry("240x480")

#rámy pro rozdělení oblastí
ram_nahore = Frame(okno)
ram_nahore.pack()
ram_registrace = Frame(okno)
ram_registrace.pack()
ram_dole = Frame(okno)
ram_dole.pack()

#horní část: titulek a obrázek
appka_jmeno = Label(ram_nahore, text="FIT–NESS APPKA")
appka_jmeno.pack()
soubor = PhotoImage(file="vzor_nvm.png")
portret = Label(ram_nahore, image=soubor, borderwidth=1, relief="solid")
portret.pack()

info_jmeno = Label(ram_nahore, text="__________")
info_jmeno.pack()

#registrační část: otázky, vstupní pole a tlačítko
dotaz_jmeno = Label(ram_registrace, text="Zadej své jméno:")
dotaz_jmeno.pack()
jmeno = Entry(ram_registrace)
jmeno.pack()
tlacitko_jmeno = Button(ram_registrace, text="Odeslat jméno", command=set_jmeno)
tlacitko_jmeno.pack()

#dolní část: otázky, vstupní pole a tlačítko
tlacitko_vyzva = Button(ram_dole, text="Chci výzvu!", command=set_vyzva)
tlacitko_vyzva.pack()

#smyčka pro vykreslení okna
okno.mainloop()