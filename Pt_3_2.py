from functools import reduce
n = int(input("Введите число: "))
lst = [1, 1]
print("Список чисел Фибоначчи:")
while lst[1] <= n:
    print(lst[1])
    x = reduce(lambda z, y: z + y, lst)
    lst[0] = lst[1]
    lst[1] = x
