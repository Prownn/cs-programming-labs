arr = [12, -3, 0, 7, -1]
print(arr)
for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = 0
print(arr)