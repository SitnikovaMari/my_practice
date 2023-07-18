import csv
kol = int(input("Сколько записей Вы хотите добавить в список? "))
new_book = []
for i in range(kol):
    name = input("Введите данные о книге\nНазвание: ")
    author = input("Введите автора книги: ")
    year = input("Введите год выпуска: ")
    row = [name, author, year]
    new_book.append(row)
with open("books.csv", "a", newline='') as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerows(new_book)
print("Данные о книгах успешно добавлены")
found_books = []
author = input("Введите автора, чьи книги хотите найти: ")
print("Найденные книги: ")
with open("books.csv", newline='') as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        if author == row["Автор"]:
            found_books.append(row)
if not found_books:
    print("В списке нет книг данного автора")
else:
    for row in found_books:
        print(row["Книга"])