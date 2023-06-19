list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]


def nat_power(n):
    for ex in range(n):
        yield 10 ** ex


list_3 = list(nat_power(6))

print(list_1)
print(list_2)
print(list_3)