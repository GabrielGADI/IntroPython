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