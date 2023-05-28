# o functie simpla care ne printeaza ceva pe ecran
# nu be da nici un raspuns (nu are return)
# nu are parametri
def printGreeting():
    print('Buna ziua! Bine ati venit')


# o functie care saluta clientul in functie de numele lui
# nu ne da nici un raspuns (nu are return)
# are nevoie de parametri

def printGreetingByName(nume, prenume):
    print(f'Buna ziua! Bine ati venit {nume} {prenume}')


# o functie care calculeaza media a 3 num
# ne da un raspuns? media numerelor da un return  (returneaza)
# ce tip de date va avea raspunsul? (3 + 3 + 4) / 3 = 3.333
def mediaNr(a, b, c):
    return (a + b + c) / 3


# o functie care ne da valoarea lui pi
# ne da un raspuns? da
# raspunsul va fi double
# are parametri
def piValue():  # pentru a se afisa codul trebuie scris deasupra return!!
    return 3.14


# daca persoana este majora returnati true, altfel false
def verificareMajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False


def verificareNr(numar):
    if numar > 0:
        return True
    else:
        return False


# zona de apelare (desktop)
printGreeting()  # // Ctrl + click pe functie => ne duce la zona de definire a metodei
printGreeting()
printGreetingByName('Cristi', 'Marius')
printGreetingByName('Ion', 'Sebi')
printGreetingByName('Vasile', 'George')
print(mediaNr(3, 3, 4))
print(piValue())
print(verificareMajor(17))
print(verificareNr(1))

# verificare : se ia un numar
numar = int(input('Introduceti numarul dorit: '))
if verificareNr(numar):
    print(f' Numarul ales este positiv!')
else:
    print(f' Acesta este un numar negativ!')

# verificare : se ia varsta utilizatorului
age = int(input('Introduceti varsta dumneavoastra: '))  # daca se afiseaza numar trebuie sa specific int
if verificareMajor(age):
    print('Cont creat cu succes!  Bine ati venit!!!')
else:
    print('Nu ai varsta minima necesara (18 ani) pentru a paria:')
