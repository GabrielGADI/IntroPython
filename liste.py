# listele in python pot sa cuprinda elemente de tipuri diferite
# au dimensiune dinamica

fructe = ['mar', 'banana', 'pere', 10, True, 10]  # listele in python pot sa cuprinda elemente de tipuri diferite
fructe.insert(3, 'bambus')
# afisam o lista
print(fructe)

#  accesam un element in functie de index
print(fructe[0])  # mar
print(fructe[1])  # banana

# adaugam un nou element
fructe.append('rosie')

# suprascriem un element
fructe[0] = 'strugure'

# afisam lista
print(fructe)

# aflam dimensiunea (len)
print(len(fructe))

# scoate si ne returneaza ultimul element
last = fructe.pop()  # pop scoate si returneaza
print('ultimul element:', last)
print('lista fructe:', fructe)

# de cate ori apare un element?
print(fructe.count(10))  # specificand elementul (10) aflam de cate ori apare

# extindem lista
fructe_exotice = ['ananas', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)
numere = {1, 45, 34, 81}
print(numere)
numere.add(49)
print(numere)
