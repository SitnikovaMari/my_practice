kilometrs = int(input("Сколько километров хотите проехать на автомобиле? "))
fuel = int(input(
    "Сколько литров топлива расходует автомобиль на 100 километров? "))
liter = int(input("Сколько литров топлива в вашем баке? "))
if (liter / fuel) * 100 >= kilometrs:
    print("Вы проедете желаемое расстояние!")
else:
    print("К сожалению, бензина не хватит.")
