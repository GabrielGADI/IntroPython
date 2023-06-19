import random


def generate_lotto_numbers(previous_numbers):
    # Generăm o listă cu toate numerele posibile
    all_numbers = list(range(1, 50))

    # Eliminăm numerele care au ieșit în extragerile anterioare
    for numbers in previous_numbers:
        for num in numbers:
            if num in all_numbers:
                all_numbers.remove(num)

    # Generăm lista cu cele 6 numere norocoase
    lucky_numbers = random.sample(all_numbers, 6)

    return sorted(lucky_numbers)


# Citim extragerile anterioare de la tastatură
previous_numbers = []
for i in range(1, 8):
    numbers = input(f"Introduceti numerele extrase la extragerea {i}: ")
    previous_numbers.append([int(x) for x in numbers.split()])

# Generăm numerele norocoase
lucky_numbers = generate_lotto_numbers(previous_numbers)

# Afisam numerele norocoase
print(f"Numerele norocoase la urmatoarea extragere sunt: {lucky_numbers}")
