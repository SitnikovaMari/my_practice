number = int(input("Введите число для проверки: "))
n = number
l= len(str(number))
summ = 0
while number != 0:
    c = number % 10
    summ = summ+(c**l)
    number = number//10
if n == summ:
    print("Число", n, "является числом Армстронга")
else:
    print("Число", n, "не является числом Армстронга")