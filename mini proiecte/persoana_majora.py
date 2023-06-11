# declaram si initializam variabila varsta de tip int
varsta = 14

# declaram variabila varsta si scriem de la tastatuta
varsta = int(input('Ce varsta aveti: '))

# in functie de o valoare se executa o singura ramura de cod
if (varsta < 0):
    print('Varsta este invalida.')
elif (varsta < 14):
    print('Minor fara buletin.')
elif (varsta < 18):
    print('Minor cu buletin.')
else:
    print('Major.')
