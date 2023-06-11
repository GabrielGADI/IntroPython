a = 5
b = "hello"
print('Valoarea lui a este:', a)  # afiseaza “Valoarea lui a este: 5”
print('Valoarea lui b este:', b)  # afiseaza “Valoarea lui b este: hello”
print('a = {}, b = {}'.format(a, b))  # afiseaza “a = 5, b = hello”

a = 5
b = "hello"
c = [1, 2, 3]
print(type(a))  # afiseaza <class ‘int’>
print(type(b))  # afiseaza <class ‘str’>
print(type(c))  # afiseaza <class ‘list’>

for i in range(999):
    if i == 3:
        break
    print(i)  # va fi afisat 0 1 2

a = 5
b = 10
if a > b:
    print("a este mai mare decât b")
else:
    print("a este mai mic sau egal decât b")

culori = ['rosu', 'albastru', 'verde', 'galben', 'mov']
for culoare in culori:
    print(f'Culoarea mea preferata este: {culoare}')

i = 0
while i <= 3:
    print(i)
    i += 1  # va fi afisat 0 1 2 3

for i in range(999):
    if i == 3:
        break
    print(i)  # va fi afisat 0 1 2

for i in range(5):
    if i == 3:
        continue
    print(i)  # va afisa 0 1 2 4, va sari peste 3


def iterare():
    for i in range(5):
        return i
    print(iterare())


def show_sum(a, b):  # parametri sunt ‘a’ si ‘b’
    print(a + b)
    show_sum(2, 5)  # parametri sunt ‘2’ si ‘5’
