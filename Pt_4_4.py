def find_combinations(lst, num, combinations=[]):
    s = sum(combinations)
    if s == num:
        print(combinations)
    if s >= num:
        return
    for i in range(len(lst)):
        n = lst[i]
        remain = lst[i + 1:]
        find_combinations(remain, num, combinations + [n])
number = int(input("Введите число: "))
N = int(input("Введите длину списка чисел: "))
lst_numbers = []
print("Заполните список числами:")
for i in range(N):
    lst_numbers.append(int(input()))
print("Найденные комбинации чисел, сумма которых равна "+str(number)+":")
print(find_combinations(lst_numbers, number))