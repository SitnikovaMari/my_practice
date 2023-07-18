import csv
def is_valid_year(year):
    try:
        year = int(year)
        if year >= 0:
            return True
        else:
            return False
    except ValueError:
        return False
fl = True
while fl:
    start_year = input("Введите начальный год: ")
    end_year = input("Введите конечный год: ")
    if not is_valid_year(start_year) or not is_valid_year(end_year) or start_year > end_year:
        print("Некорректный ввод годов. Введите еще раз.")
    else:
        start_year = int(start_year)
        end_year = int(end_year)
        with open('books.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter=";")
            books = []
            for row in reader:
                for year in range(start_year, end_year + 1):
                    year = str(year)
                    if year == row["Год выпуска"]:
                        books.append(row)
            if not books:
                print("В списке нет книг этих годов")
            else:
                print("Книги, выпущенные с", start_year, "по", end_year, ":")
                for book in books:
                    print(book["Книга"], "|", book["Автор"], "|", book["Год выпуска"])
        fl = False