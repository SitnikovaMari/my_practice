import random
lst = []
n = int(input("Введите длину списка: "))
while n > 0:
    c = random.randint(1, 1000)
    a = 0
    for i in range(2, c-1):
        if c % i == 0:
            a += 1
            if a > 0:
                lst.append(c)
                n = n-1
                break
print(lst)