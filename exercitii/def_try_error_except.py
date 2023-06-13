# se ia valoarea de la foo si se transforma valoarea la patrat (x, x)
def foo(x, y):
    return x * y


def bar(x):
    return foo(x, x)


print(bar(8) + bar(3))

print(20 * " - ", "Exercitiul 1", 20 * " - ")


# result 100
def foo(x, y=2):
    return x ** y


print(foo(10))

print(20 * " - ", "Exercitiul 2", 20 * " - ")

# 0,1
def foo(x):
    x += 1
    return x


a = 0
b = foo(a)
print(a, b)

print(20 * " - ", "Exercitiul 3", 20 * " - ")

# TypeError
# def func(x, y, z):
#     print(x, y, z)
#
# my_list = [1, 2, 3, 4, 5]
#
# func(*my_list)

print(20 * " - ", "Exercitiul 4 TypeError", 20 * " - ")

# class Foo:
#     def __mit__(self, x):
#         self.x = x
#     def __eq__(self, other):
#         return self.x == other.x
#
# foo1 = Foo(2)
# foo2 = Foo(1)
#
# print(foo1 is foo2)
# print(foo1 == foo2)

print(20 * " - ", "Exercitiul 5", 20 * " - ")


# a doua litera va fi inlocuita peste tot in cuvant cu "c"
def mystery_function(word):
    vowels = "aeiou"
    for i in range(len(word)):
        if word[i] in vowels:
            word = word[:i] + "c" + word[i + 1:]
    return word


new_word = mystery_function("capaybara")

print(new_word)

print(20 * " - ", "Exercitiul 6", 20 * " - ")


# afiseaza cate o cifra(next(gen)) si celelalte cifre in lista(lis(gen))
def get_numbers(n):
    for i in range(n):
        yield i


gen = get_numbers(9)
print(next(gen))  # prima cifra
print(next(gen))  # a doua cifra
print(list(gen))  # urmatoarele cifre fara ultima in lista

print(20 * " - ", "Exercitiul 7", 20 * " - ")
