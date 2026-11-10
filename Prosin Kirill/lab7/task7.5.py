rows, columns = map(int, input().split())
table = []
for i in range(rows):
    table.append([int(value) for value in input().split()])
res = [int(part) for part in input().split()]
num = int(input())
for row in range(len(table)):
    for column in range(len(table[row])):
        if (row < res[0] or row > res[1]) or (column < res[2] or column > res[3]):
            table[row][column] = 0
j = 0
count = False
for row in table:
    i = 0
    for value in row:
        if value == num:
            print(j, i)
            count = True
        i += 1
    j += 1
if count == False:
    print("Не найдено")
