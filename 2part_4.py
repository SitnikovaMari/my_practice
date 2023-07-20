import math
input("Введите значения коэффициентов квадратного уравнения:")
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
D = b ^ 2 - 4 * a * c
print("Ответ:")
if D < 0:
    print("Корней нет")
elif D == 0:
    print("Корень один: ", -b // (2 * a))
else:
    print("Первый корень: ", (-b + math.sqrt(D)) // (2 * a))
    print("Второй корень: ", (-b - math.sqrt(D)) // (2 * a))
