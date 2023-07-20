listt = ['импровизация', 'голос', 'танцы', 'орел и решка']
print("Список телевизионных передач: ")
print(listt[0], listt[1], listt[2], listt[3], sep="\n")
tv = input("Введите любую телепередачу: ")
pos = int(input("Введите позицию, на которую добавить передачу: "))
listt.insert(pos - 1, tv)
print("Измененный список телевизионных передач: ")
for i in range(len(listt)):
    print(listt[i])
