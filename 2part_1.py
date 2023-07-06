import random
input("красный, зеленый, желтый, синий, розовый")
red = "красный"
green = "зеленый"
yellow = "желтый"
blue = "синий"
pink = "розовый"
color = random.choice([red, green, yellow, blue, pink])
fl = True
while fl:
    color_user = input("Выберите один цвет из списка: ")
    if color == color_user:
        print("Отлично!")
        fl = False
    elif color == red:
        print("Подсказка: помидор")
    elif color == green:
        print("Подсказка: трава")
    elif color == yellow:
        print("Подсказка: солнце")
    elif color == blue:
        print("Подсказка: небо")
    elif color == pink:
        print("Подсказка: барби")