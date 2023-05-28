# afisare 101  dalmatieni unu cate unu
for i in range(1, 102):
    print(f'Dalmatianul cu numarul : {i}')

# afisare 101 dalmatieni din 2 in 2
for i in range(1, 102, 2):
    print(f'Dalmatianul cu numarul : {i}')

#  ne ajuta sa parcurgem un array prin intermediul indexului
numere = [3, 7, 10, 20, 35]

# parcurgere lista cu for prin intermediul index
for i in range(0, len(numere)):
    print(f' Indexul  curent este {i}')
    print(f' Numarul  curent este {numere[i]}')

# parcurgem array de culori
culori = {'Alb', 'Albastru', 'Verde', 'Portocaliu'}
for culoare in culori:
    print('Culoarea mea preferata este ' + culoare)  # arata fiecare culoare separat
print(culori)  # afisearaza ce contine array

# for each suma numerelor in array
s = 0
for numar in numere:
    print(f' numarul curent este: {numar}')
    s = s + numar
    print(f' numere {s}')  # imi arata suma pe fiecare etapa in parte
print(f'suma este {s}')  # imi arata suma finala
