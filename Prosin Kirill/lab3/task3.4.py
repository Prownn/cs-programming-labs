train = input("Введите данные о поезде одной строкой в формате номер;откуда;куда;время;цена")
train = train.split(";")
print(train)
print(f"""
    Поезд: {train[0]}
    Маршрут: {train[1]} - {train[2]}
    Отправление: {train[3]}
    Цена: {train[4]}
    """)