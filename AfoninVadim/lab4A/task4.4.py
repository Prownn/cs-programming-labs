f_side = int(input())
s_side = int(input())
t_side = int(input())

if (f_side or s_side or t_side <= 0) or (f_side + s_side < t_side) or (f_side + t_side < s_side) or (s_side + t_side < f_side) :
    print('Треугольник не существует')
else:
    if f_side == s_side == t_side:
        print('Равносторонний')
    elif f_side == t_side or t_side == s_side or f_side == s_side:
        print('Равнобедренный')
    else:
        print('Разносторонний')
