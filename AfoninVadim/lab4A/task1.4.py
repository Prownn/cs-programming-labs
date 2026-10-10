current = float(input('Текущая \n'))
des = float(input('Желаемая \n'))

if current > des:
    print('Охлаждение')
elif current < des:
    print('Нагрев')
elif current == des:
    print('Выключен')