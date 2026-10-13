train = input()
train = train.split(";")
print(f"""
    Поезд: {train[0]}
    Маршрут: {train[1]} - {train[2]}
    Отправление: {train[3]}
    Цена: {train[4]}
    """)
