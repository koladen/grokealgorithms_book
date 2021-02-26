# РЕКУРСИВНЫЙ ФАКТОРИАЛ
# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x * fact(x-1)
#
#
# print(fact(3))

# БЫСТРАЯ СОРТИРОВКА
import random
import time


def timer_check(func): # Декоратор вычисления времени выполнения для рекурсивной функции
    funcs_eval = set() # В этом множестве будем запоминать имя функции, которую вызвали

    def inner(*args):

        if func.__name__ not in funcs_eval: # Если функция вызывается первый раз, запомним ее имя в множестве, чтобы не
            funcs_eval.add(func.__name__)   # вызывать подсчет времени на каждом вызове рекурсии
            start = time.time()
            result = func(args[0])

            stop = time.time()
            print("работали", (stop-start))
            return result
        else:
            return func(args[0])    # Если имя функции уже есть в множестве, просто вернем ее результат
    return inner


def profile(f):
    is_evaluating = False
    def g(x):
        nonlocal is_evaluating
        if is_evaluating:
            return f(x)
        else:
            start_time = time.time()
            is_evaluating = True
            try:
                value = f(x)
            finally:
                is_evaluating = False
            end_time = time.time()
            print('time taken: {time}'.format(time=end_time-start_time))
            return value
    return g

# @profile
@timer_check
def fast_sort(arr):
    arr = list(arr)  # Не портим исходный массив
    if len(arr) < 2:
        return arr
    else:
        key_element_index = random.randrange(0, len(arr))  # Опроный элемент выбираем случайно, так эффективнее
        key_element = arr.pop(key_element_index)
        less = [i for i in arr if i <= key_element]
        high = [i for i in arr if i > key_element]
        return fast_sort(less) + [key_element] + fast_sort(high)  # Рекурсивно продолжаем сортировку
#
#
# my_arr = [3, 1, 1, 1, 1, 2, 2, 7, 19, 4, 12, 5]
# print(fast_sort(my_arr))
# print(my_arr)

# РЕКУРСИВНЫЕ ФУНКЦИИ
def recursive_sum(arr):
    arr = list(arr)
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + recursive_sum(arr[1:])


def recursive_count(arr):
    arr = list(arr)
    if len(arr) == 1:
        return 1
    else:
        return 1 + recursive_count(arr[1:])


def recursive_max(arr):
    arr = list(arr)
    if len(arr) == 1:
        return arr[0]
    else:
        max = arr[0]
        if max > recursive_max(arr[1:]):
            return max
        else:
            return recursive_max(arr[1:])


def recursive_binary_search(arr, target, index):
    if len(arr) == 1:
         if arr[0] == target:
             return index[0]
         else:
             return None
    else:
        arr = list(arr)
        index = list(index)
        low = 0
        high = len(arr) - 1
        mid = int((low + high) / 2)
        if arr[mid] == target:
            return index[mid]
        elif arr[mid] > target:
            return recursive_binary_search(arr[0:mid], target, index[0:mid])
        else:
            return recursive_binary_search(arr[mid+1:], target, index[mid + 1:])



# my_arr = [1, 2, 10, 17, 18, 19, 22]
# print(recursive_binary_search(my_arr, 17, [n for n, i in enumerate(my_arr)]))

my_new_arr = [random.randrange(0, 10000) for i in range(10000)]

fast_sort(my_new_arr)
