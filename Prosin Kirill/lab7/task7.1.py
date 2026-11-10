arr = [int(part) for part in input().split()]
print("Исходные остатки:", arr)
for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = 0
print("Исправленные остатки:", arr)

