a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
summ = 0
for i in range(a, b + 1):
    summ += i
print("Сумма всех целых чисел от "
      "" + str(a) + " до " + str(b) + " равна " + str(summ))
