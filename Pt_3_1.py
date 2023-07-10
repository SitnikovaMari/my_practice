import random
lst = []
n = int(input("Введите длину списка чисел: "))
for i in range(n):
    lst.append(random.randint(2, 50))
print(lst)
sred = lambda l, n: sum(l)/n
print("Среднее значение списка чисел: ", sred(lst, n))