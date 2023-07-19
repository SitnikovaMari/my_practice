name = input("Введите свое имя: ")
age = int(input("Введите свой возраст: "))
if age % 10 == 1:
    print("Привет, " + name + "! Тебе уже " + str(age) + " год.")
if age % 10 == 2 or age % 10 == 3 or age % 10 == 4:
    print("Привет, " + name + "! Тебе уже " + str(age) + " года.")
if (age % 10 == 0 or age % 10 == 5 or age % 10 == 6 or
        age % 10 == 7 or age % 10 == 8 or age % 10 == 9):
    print("Привет, " + name + "! Тебе уже " + str(age) + " лет.")
