import time
import random as rd

def sort_list_imperative(numbers: list):
    lst = numbers.copy()
    is_sorted = False
    if not is_sorted:
        for i in range(len(lst) - 1):
            for j in range(len(lst) - i - 1):
                if lst[j] < lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


def sort_list_imperative_insert(numbers: list):
    lst = numbers.copy()
    start = time.time()
    print(start)
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] > lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    stop = time.time()
    print(stop)
    time_dif = start - stop
    return lst, f'{time_dif:.3f}'


def sort_list_declarative(numbers: list):
    numbers = sorted(numbers, reverse=True)
    return numbers


def sort_list_declarative_insert(numbers: list):
    numbers.sort(reverse=True)
    return numbers


if __name__ == '__main__':
    # print(sort_list_imperative([3, 6, 7, 9, 0, 100, 8, 1000]))
    temp_lst = []
    for i in range(100):
        i = rd.randint(0, 1000)
        temp_lst.append(i)
    print(sort_list_imperative_insert(temp_lst))
        # [3, 6, 7, 9, 0, 100, 8, 1000, 444, 890, 45, 99, 77, 88, 5, 78, 90, 93, 55, 55, 3, 6, 7, 9, 0, 100, 8, 1000, 444,
        #  890, 45, 99, 77, 88, 5, 78, 90, 93, 55, 555, 3, 6, 7, 9, 0, 100, 8, 1000, 444, 890, 45, 99, 77, 88, 5, 78, 90,
        #  93, 55, 556, 3, 6, 7, 9, 0, 100, 8, 1000, 444, 890, 45, 99, 77, 88, 5, 78, 90, 94, 55, 586, 3, 60, 71, 9, 0, 100,
        #  8, 1000, 444, 890, 45, 99, 77, 88, 5, 78, 90, 93, 55, 555, 3, 6, 7, 9, 0, 100, 8, 1000, 444, 890, 45, 99, 77,
        #  88, 5, 78, 90, 93, 55, 57, 3, 6, 7, 9, 0, 100, 8, 1000, 44, 890, 450, 99, 77, 88, 5, 78, 90, 93, 55, 555, 3,
        #  61, 70, 90, 0, 100, 8, 1000, 478, 890, 45, 99, 77, 88, 5, 78, 90, 934, 55, 555]))
    # print(sort_list_declarative([3, 6, 7, 9, 0, 100, 8, 1000]))
    # print(sort_list_declarative_insert([3, 6, 7, 9, 0, 100, 8, 1000]))
