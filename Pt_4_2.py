def palindrom(c):
    palindromes = []
    for i in range(len(c)):
        for j in range(i+1, len(c)+1):
            s = c[i:j]
            reversed_s = "".join(reversed(s))
            if s == reversed_s:
                if len(s) > 1:
                    palindromes.append(s)
    return palindromes
content = input("Введите строку: ")
palindromes = palindrom(content)
print("Палиндромы, найденные в строке:")
for i in range(len(palindromes)):
    print(palindromes[i])