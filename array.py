numere = [2, 3, 7, 2, 2]
elevi = ['Gigel', 'Costica', 'Ion', 'Adi', 'Manole']
print(elevi[2], elevi[1], elevi[3], numere[0], numere[2])  # afisare continu array
print(numere.count(2))  # de cate ori se repeta 2
elevi[0] = 'Marin'  # suprascriere
numere[3] = 8  # suprascriere
print(f'The last place is: ' + elevi[len(elevi) - 1])  # sa printam ultimul element mereu
print(numere)
print(len(elevi))  # printam dimensiue array
note = [0, 0, 0, 0, 0]
note[0] = 10
note[1] = 9
print(note[1])
print(numere[1])
print(f'The last place is: ' + elevi[len(elevi) - 1] + ' ' 'with nota : 10')
