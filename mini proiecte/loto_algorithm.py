import random

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ]
lista1 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
lista2 = [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

print(20 * " - ", "lista nr1", 20 * " - ")
lista = lista + lista1 + lista2
nr1 = random.choice(lista)
lista.remove(nr1)
print(nr1)
print(lista)

print(20 * " - ", "lista nr2", 20 * " - ")
nr2 = random.choice(lista)
lista.remove(nr2)
print(nr2)
print(lista)

print(20 * " - ", "lista nr3", 20 * " - ")
nr3 = random.choice(lista)
lista.remove(nr3)
print(nr3)
print(lista)

print(20 * " - ", "lista nr4", 20 * " - ")
nr4 = random.choice(lista)
lista.remove(nr4)
print(nr4)
print(lista)

print(20 * " - ", "lista nr5", 20 * " - ")
nr5 = random.choice(lista)
lista.remove(nr5)
print(nr5)
print(lista)

print(20 * " - ", "lista nr6", 20 * " - ")
nr6 = random.choice(lista)
lista.remove(nr6)
print(nr6)
print(lista)

print(20 * " - ", "lista nr7", 20 * " - ")
nr7 = random.choice(lista)
lista.remove(nr7)
print(nr7)
print(lista)

print(20 * " - ", "lista nr1,nr2,nr3,nr4,nr5,nr6,nr7", 20 * " - ")
print(nr1, nr2, nr3, nr4, nr5, nr6, nr7)
