base_cost = float(input('Базовая цена \n'))
age = int(input('Возраст \n'))

if base_cost < 0 or age > 120 or age < 0:
    print('Ошибка')
elif 0 <= age <= 5:
    print(f'{base_cost * 0:.2f}')
elif 6 <= age <= 17:
    print(f'{base_cost / 2:.2f}')
elif 18 <= age <= 59:
    print(f'{base_cost:.2f}')
elif age > 59:
    print(f'{base_cost * 0.7:.2f}')
