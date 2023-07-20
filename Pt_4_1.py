n = int(input("Введите число: "))
num = list(str(abs(n)))
if n >= 0:
    num.sort(reverse=True)
    print("Максимальное число:", "".join(num))
else:
    num.sort()
    print("Максимальное число:", int("".join(num)) * (-1))
