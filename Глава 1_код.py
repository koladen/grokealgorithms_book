# БИНАРНЫЙ ПОИСК
def binary_search(sequence, item):
    low = 0
    high = len(sequence) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = sequence[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 2, 3, 5, 9, 11, 12]
print(binary_search(my_list, 13))

