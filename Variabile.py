# variable- zona din memorie care tine date

# am declarat si initializat variabila marca
marca_masina = 'volvo'
model_masina = 'Xc 60'

# nu putem sa punem spatiu in numele variabilei
# o variabila incepe cu litera mica

# looesly typed - nu trebuie sa specificam tipurile de date

print(f'Am cumparat o masina marca : {marca_masina}')
print(f'Este modelul : {model_masina}')

# suprascriere
model_masina = 'XC 60 facelift'
print(f'Am cumparat o masina marca : {marca_masina}')
print(f'Este modelul : {model_masina}')

nume = 'Gabriel'
prenume = 'Domiteanu'
varsta = 37
# concatenare de stringuri
print(prenume + ' ' + nume)
print(f'Ma cheama {nume} {prenume} si am varsta de {varsta}')
print(f'{marca_masina}')
