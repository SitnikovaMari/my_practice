n1 = int(input("Введите первое число: "))
n2 = int(input("Введите второе число: "))
n3 = int(input("Введите третье число: "))
if n1 >= n2 and n1 >= n3:
    maxx = n1
    if n2 >= n3:
        minn = n3
    else:
        minn = n2
elif n2 >= n1 and n2 >= n3:
    maxx = n2
    if n1 >= n3:
        minn = n3
    else:
        minn = n1
else:
    maxx = n3
    if n1 >= n2:
        minn = n2
    else:
        minn = n1
sred = (n1 + n2 + n3) - maxx - minn
print("Максимальное число: " + str(maxx))
print("Все три числа по убыванию :", maxx, sred, minn)