n = int(input("Введите число: "))
for i in range(1, 1000000000000):
    if i*i > n:
        break
print(i)