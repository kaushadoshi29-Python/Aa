arr = [29, 10, 14, 37, 13]

n = len(arr)

for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j

    # Swap elements
    temp = arr[i]
    arr[i] = arr[min_idx]
    arr[min_idx] = temp

# Print the sorted array
for i in range(n):
    print(arr[i], end=" ")