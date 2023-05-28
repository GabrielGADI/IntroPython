# declaram si initializam un dict
note_elevi = {'Gigel': 10, 'Costel': 9, 'Ana': 10}

# adaugare elemente
note_elevi['Sebi'] = 8

# printam dictul
print(note_elevi)

# aflam elemente din dict
print(note_elevi['Gigel'])
print(note_elevi.get('Gigel'))  # o metoda mai complexa

# actualizam valori
note_elevi['Sebi'] = 10
print(note_elevi)

# aflam dimensiunea
print(len(note_elevi))

# stergem valori
note_elevi.pop('Gigel')  # cu extensia .pop putem sterge valori
print(note_elevi.get('Gigel', 'nu mai avem acest elev : Gigel'))  # putem continua sa scriem dupa, un mesaj
print(note_elevi)

# returneaza doar cheile
print(note_elevi.keys())
