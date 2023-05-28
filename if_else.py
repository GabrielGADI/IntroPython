# Flow control - if else
# evalueaza si bifurca codul in functie de rezultat
# if
piesa_faina = True  # // invat calculatorul daca piesa e faina sau nu
print('pornim radio')
if piesa_faina == True:
    print('dam mai tare radioul')  # daca piesa e frumoasa, dau mai tare
    print('incep sa o fredonez')
else:
    print('oprim radio')

# if else
# daca numarul este par printam acest lucru
# altfel printam impar

numar = int(input(f'Scrieti va rog un numar: '))
# ce insemna par? se imaprte exact la 2
# ce insemna ca se imparte la 2? impartirea ne da restul 0
if numar % 2 == 0:
    print('numar par')
else:
    print('numar impar')

# este un numar pozitiv?
numar = int(input('Alegeti un numar pozitiv: '))
if numar > 0:
    print('pozitiv')
else:
    print('negativ')

# if, else if, else
# cum ne saluta robotelul in functie de ora?

# luam date de la tastatura
# ne asiguram ca sunt transformate din string in int
ora = int(input('Introdu ora: '))
print(ora == 17)
if ora < 0:
    print(' !!!Ora invalida.Ora negativa!!!')
elif ora <= 11:
    print('Buna Dimineata!')
elif ora <= 18:
    print('Buna ziua!')
elif ora <= 21:
    print('Buna Seara!')
elif ora <= 24:
    print('Noapte Buna!')
else:
    print(' !!!Ora mai mare decat 24.Ora Invalida!!!')

# robotel telefonic
optiunea = int(input('Alege o optiune'))
if optiunea == 0:
    print('Meniu anterior!')
elif optiunea == 1:
    print('Ati ales limba romana!')
elif optiunea == 2:
    print('Ati ales limba engleza!')
else:
    print('Nu s-a identificat optiunea.Mai incercati, va rog!')
