rows, columns = map(int, input().split())
table = []
for i in range(rows):
    table.append([int(value) for value in input().split()])
row_sums = []
for row in table:
    total = 0
    for value in row:
        total += value
    row_sums.append(total)
column_sums = []
for column in range(columns):
    total = 0
    for row in range(rows):
        total += table[row][column]
    column_sums.append(total)
print(f"Суммы строк: {row_sums} \nСуммы столбцов: {column_sums}")
