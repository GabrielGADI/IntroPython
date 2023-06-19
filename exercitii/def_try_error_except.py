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


# afiseaza suma
def func(x, y, z):
    return x + y + z


params = [1, 2, 3]
result = func(*params)

print(result)

print(20 * " - ", "Exercitiul 8", 20 * " - ")

# type error
# x = 5
# y = "2"
# result = x + y
# print(result) # TypeError

print(20 * " - ", "Exercitiul 9", 20 * " - ")

# IndexError
# nums = [1, 2, 3, 4, 5]
# for i in range(len(nums)):
#     if nums[i] == 3:
#         nums.pop(i)
# print(nums)

print(20 * " - ", "Exercitiul 10 IndexError", 20 * " - ")

# TypeError
# def func(a, b):
#      return a * b
# result = func(2, 3)
# result = result(4, 5)
#
# print(result)
print(20 * " - ", "Exercitiul 11 TypeError", 20 * " - ")

# IndexError - nu avem al 5-lea element in lista
# nums = [1, 2, 3, 4, 5]
# squares = [num**2 for num in nums]
# print(squares[5])
#


print(20 * " - ", "Exercitiul 12 IndexError", 20 * " - ")

# Oops! invalid literal for int() with base 10: 'a'
try:
    x = int('a')
except ValueError as e:
    print("Oops!", e)

print(20 * " - ", "Exercitiul 13", 20 * " - ")


# None
def divide(x, y):
    try:
        result = x / y
    except:
        result = None
    return result


print(divide(10, 0))

print(20 * " - ", "Exercitiul 14", 20 * " - ")
