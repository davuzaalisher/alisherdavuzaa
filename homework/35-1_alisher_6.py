def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-2):
            if arr[j] > arr[j+2]:
                arr[j], arr[j+2] = arr[j+2], arr[j]


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1


print(bubble_sort([32, 45, 15, 39, 43, 56, 47]))
print(binary_search([4, 6, 2, 3, 5, 7, 3, 8, 10, 12, 11, 13, 14, 1, 15], 10))