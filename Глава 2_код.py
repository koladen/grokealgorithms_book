def find_smallest(arr):
    smallest = arr[0]
    smal_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smal_index = i
    return smal_index


def my_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr.pop(find_smallest(arr)))

    return new_arr

print(my_sort([7, 19, 1, 3]))