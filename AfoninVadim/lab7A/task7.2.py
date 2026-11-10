list = [-3, 5, 0, 2, 1, 5]
list1 = []
for i in list:
    if i > 0 and i % 2 != 0:
        list1.append(i**2)
    else:
        continue
print('Квадраты:', list1)
