dist = int(input("Введите расстояние: ")) / 100
cons = float(input("Введите расход: "))
cost = float(input("Введите цену: "))
print(f"Топливо: {dist * cons:.2f} л")
print(f"Стоимость: {dist * cons * cost:.2f} руб")