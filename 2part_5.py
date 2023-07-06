import random
win = lose = 0
fl = True
while fl:
    if lose == 3:
        print("Игра завершена")
        fl = False
    else:
        n = random.randint(0, 1)
        print("Выбор компьютера: ", n)
        user = int(input("Орел или решка? "))
        if user != 0 and user != 1:
            print("Игра закончена")
            fl = False
        elif user == n:
            win += 1
            lose = 0
        elif user != n:
            lose += 1