n = int(input("Введите число: "))
is_even = lambda n: n % 2 == 0
if is_even(n):
    print("Число чётное")
else:
    print("Число нечётное")