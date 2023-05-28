'''
Recap:
variabile - zone din memorie care tin anumite date
tipuri de date: char - un caracter de la tasttura,
string - sir de caractere delimitate de " ",
integer(int) - numar intreg,
float - numar zecimal in python (3.2),
double - numar zecimal in java (3.2),
boolean - adevarat sau fals (true sau false in Java)
boolean - adevarat sau fals (True sau False in Python)

Operatori:
aritmetici: +, -, *, /, %
de comparare: < >, ==, !=, >=, <=,
logici:and (SI), or(SAU), !(NOT)
'''

a = 3
b = 9
print(a / b)  # 3 / 9 => 0.3333333
print(a * b)  # 3*9 => 27
print(a == b)  # 3=9? False
print(a != b)  # 3 diferit de 9? =>True
print(a < b and a < 6)  # 3<9 (True) SI 3<6 (True)? => True
print(a < b or a < 2)  # 3<9 (True) SAU 3<2 (False)? => True
print(a % b)  # 3 % 9 => 3

# cu mama sau tata sau (bunicu si bunica)
mama = True
tata = True
bunicu = False
bunica = False
print(mama or tata or (bunicu and bunica))
