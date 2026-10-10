inf = str(input())
inf = inf.replace(';', ' ').split(' ')
print(inf)
print(f'''
Поезд: {inf[0]}
Маршрут: {inf[1]}  -  {inf[2]}
Отправление: {inf[3]}
Цена: {inf[4]}
''')
