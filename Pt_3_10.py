d = {}
s = input("Введите строку: ")
for i in s:
    if i != " ":
        count = 0
        for symbol in s:
            if i == symbol:
                count += 1
                d[symbol] = count
print(d)