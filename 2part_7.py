summ = 0
fl = True
while fl:
    n = int(input("Введите число: "))
    if n < 0:
        summ += n
    else:
        fl = False
print("Полученная сумма: ", summ)