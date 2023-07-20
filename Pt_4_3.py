n1 = int(input("Введите превое число диапазона: "))
n2 = int(input("Введите второе число диапазона: "))
print("Простые числа заданного диапазона:")
for i in range(n1, n2 + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
