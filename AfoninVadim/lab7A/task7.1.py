list = [12, -3, 0, 7, -1]
list1 = []
for i in list:
    if i >= 0:
        list1.append(i)
    else:
        list1.append(0)
print(f'''
Исходные остатки: {list}
Исправленные остатки: {list1}
''')
