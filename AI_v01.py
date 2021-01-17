print("Cześć, jestem programem, który może w przyszłości będzie potrafił się czegoś uczyć.\n")
imie = input("Jak masz na imię?\n")
#if imie in ['Blazej','Błażej']:
uzytkownicy = open("uzytkownicy.txt","r+")
uzytkownicy_lista = uzytkownicy.read()

if imie in uzytkownicy_lista:

    print ("Wszystko gra, jedziemy dalej "+imie)
    print ("Co byś chciał zrobić dzisiaj ?")
    zadania = open("zadania.txt", "r+")
    zadania_zawartosc = zadania.read()
    print (zadania_zawartosc)
    zadania.close()
    uzytkownicy.close()
else:
    print ("Mamy kogoś nowego na pokładzie\n Witaj "+imie)
    uzytkownicy = open("uzytkownicy.txt","a+")
    uzytkownicy_zapisz = uzytkownicy.write('\n'+imie)
    uzytkownicy.close()
