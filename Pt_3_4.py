import random
lst = []
n = int(input("Введите длину списка чисел: "))
for i in range(n):
    lst.append(pow(random.randint(1, 60), 2))
print("Список квадратов рандомных чисел: ", lst)
