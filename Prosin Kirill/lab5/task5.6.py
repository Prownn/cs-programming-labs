n = int(input())
count = 0
for i in range(n):
    row = []
    val = 1
    for j in range(i + 1):
        row.append(str(val))
        if val % 2 != 0:
            count += 1
        val = val * (i - j) // (j + 1)
    print(" ".join(row))
print(f"Нечетных элементов: {count}")
