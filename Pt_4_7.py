import itertools
from random import randint
N = int(input("Введите длину списка чисел: "))
lst = []
for i in range(N):
    lst.append(randint(1, 100))
print("Список из рандомных чисел: ", lst)
print("Все перестановки списка чисел:")
print(list(itertools.permutations(lst)))
