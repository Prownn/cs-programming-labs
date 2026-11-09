arr = [-3, 5, 0, 2, 1, 5]
new_arr = []
for i in range(len(arr)):
    if arr[i] > 0 and arr[i] % 2 == 1:
        new_arr.append(arr[i]**2)
print("Квадраты:", new_arr)
