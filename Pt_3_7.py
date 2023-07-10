d = {}
vowels = 'аеёиоуыэюя'
for i in input("Введите строку: "):
    if i != " ":
        if i in vowels:
            d[i] = True
        else:
            d[i] = False
print(d)