current = float(input('Текущая \n'))
desirable = float(input('Желаемая \n'))

if current > desirable:
    print('Охлаждение')
elif current < desirable:
    print('Нагрев')
elif current == desirable:
    print('Выключен')