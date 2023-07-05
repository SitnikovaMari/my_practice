number = int(input("Введите число от 10 до 20: "))
while number < 10 or number > 20:
    if number < 10:
        number = int(input("Число меньше требуемого диапазона. Введите число ещё раз: "))
    elif number > 20:
        number = int(input("Число больше требуемого диапазона. Введите число ещё раз: "))
print("Спасибо")