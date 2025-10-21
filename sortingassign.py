def bubble_sort_desc(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort_desc([1, 3, 4, 5, 6, 2, 9, 0, 7]))
print(bubble_sort_desc([67, 0, 67, -7, 3, 2, 1, 7, 999]))


#if we sort the strings if we give the answer based on the dictionary order


# bubble  sort based on the length
def bubble_sort_strings(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort_strings(["apple", "bat", "car", "dog", "elephant", "fan"]))

def bubble_sort_by_length(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if len(arr[j]) > len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort_by_length(["apple", "bat", "car", "dog", "elephant", "fan"]))

bubble sort Can you sort nested lists based on the first element of each nested list.
def bubble_sort_nested(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort_nested([[1, 56, 56], [90, 79, 98], [78, 86, 72], [6, 13, 42], [89, 7, 5]]))






