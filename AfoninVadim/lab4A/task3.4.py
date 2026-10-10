x = float(input('\n'))
y = float(input('\n'))

if x == 0 and y == 0:
    print('Начало координат')
elif y == 0 and x != 0:
    print('Ось Х')
elif x == 0 and y != 0:
    print('Ось Y')
elif x >0 and y >0:
    print('I четверть')
elif x< 0 and y > 0:
    print('II четверть')
elif x and y < 0:
    print('III четверть')
elif x > 0 and y < 0:
    print('IV четверть')

