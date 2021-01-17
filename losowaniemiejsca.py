import tkinter as tk
import random

TYTUL = "Losowanie miejscowki"
MIEJSCOWKI = [
"Budny Brzeg",
"Ladowe Ladowiska",
"Leniwa Laguna",
"Oaza Spokoju",
"Pagody Pomyslonsci",
"Przyjemny Park",
"Rozdroza Rupieci",
"Samotne Schronisko",
"Sielskie Siodlo",
"Sklepowa Sadyba",
"Slone Strzechy",
"Sloneczne Stopnie ",
"Srogi Szczyt",
"Szemrane Szyby",
"The Block",
"Widmowe Wzgorza",
"Wykrzywione Wieze",
"Wypasiona Wyrwa",
"Zalew Zdobyczy",
"Zgubne Ziemie",
"Meksyk",
"Viking",
]
PRZYCISKI = [
"Pokaz zaznaczone",
"Losuj z zaznaczonych",
]


#
#   Ustawiam Tkinter
#
okno = tk.Tk()
okno.title(TYTUL)


#
#	Funkcje
#

def czysc_ekran():
    # Ta funkcja wyczysci pole tekstowe z calego tekstu
    ekran.delete('1.0', "end")

def aktu_ekran(zawartosc):
    # Ta funkcja wypisuje "zawartosc" w polu tekstowym
    ekran.insert("end", zawartosc + "\n")

def zbierz_zaznaczone():
    # Zbiera te wartosci, które zostaly zaznaczone
    zebrane = []
    for x in dic_miejscowki.items():
        if x[1].get() == True:
            zebrane.append(x[0])
    return zebrane

def pokaz_zaznaczone():
    # Wypisuje w polu tekstowym wszystkie zaznaczone wartosci
    if zbierz_zaznaczone():
        czysc_ekran()
        aktu_ekran("Zaznaczone są:")
        for x in zbierz_zaznaczone():
            aktu_ekran(x)
    else:
        aktu_ekran("Brak zaznaczonych miejsc!")

def losuj_z_zaznaczonych():
    # Wypisuje w polu tekstowym wartosc losowo wybrana z zaznaczonych wartosci
    if zbierz_zaznaczone():
        czysc_ekran()
        wybraniec = random.choice(zbierz_zaznaczone())
        aktu_ekran("Wybranym losowo miejscem jest:")
        aktu_ekran(wybraniec)
    else:
        aktu_ekran("Brak zaznaczonych miejsc!")


#
#   Ustawiam Framy
#

frame_l   = tk.Frame(okno)
frame_l.pack(side = "left", fill = "both")

frame_r  = tk.Frame(okno)
frame_r.pack(side = "right", fill = "both")


#
#   Ustawiam lewy Frame
#   Lista checkboxów
# W tym Frame zastosuje .pack() do organizacji

# Slownik dajacy kazdej miejscowce jej wlasne tk.IntVar()
dic_miejscowki = {}
for x in MIEJSCOWKI:
    dic_miejscowki[x] = tk.IntVar()

# Checkboxy
for x in dic_miejscowki.items():
    tk.Checkbutton(frame_l, text = x[0], variable = x[1], anchor = "w").pack(side = "top", fill = "both")


#
#   Ustawiam prawy Frame
#   Pole tekstowe i przyciski
# W tym Frame zastosuje .grid() do organizacji

# Pole tekstowe
ekran = tk.Text(frame_r, height = 25, width = 40)
ekran.grid(row = 0, column=0, columnspan=5)

# Przyciski
tk.Button(frame_r, text = PRZYCISKI[0], command = lambda:pokaz_zaznaczone()).grid(row = 1, column = 0)

tk.Button(frame_r,text = PRZYCISKI[1],command= lambda:losuj_z_zaznaczonych()).grid(row = 1 , column = 1)


#
#   Tkinter mainloop
#
okno.mainloop()
