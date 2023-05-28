'''
Calculator impozit masina
In functie de cm cubi ai masinii, dorim sa afisam impozitul
    - cc < 0 => invalid
    - cc < 1000 =>70.50 lei
    - cc < 2400 => 159.90 lei
    - pentru restul valorilor => 900 lei

Tema
Declarati variabile pentru marca si model
Expuneti propozitia: "Pentru masina marca x model y, impozitul este de z lei."

'''

# ce variabile avem nevoie? ce tip de date?
cc = 1000
impozit = 0

# ca sa scriem de la tastatura:
cc = int(input("cc este: "))

# ce structura avem nevoie ca sa calculam impozitul?
if (cc < 0):
    print("Valoarea cc invalida.")
elif (cc < 1000):
    impozit = 70.50
elif (cc < 2400):
    impozit = 159.90
else:
    impozit = 900
# afisare impozit
print(f"Impozitul dvs este de {impozit} lei.")
