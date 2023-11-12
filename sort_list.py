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
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] > lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst


def sort_list_declarative(numbers: list):
    numbers = sorted(numbers, reverse=True)
    return numbers


def sort_list_declarative_insert(numbers: list):
    numbers.sort(reverse=True)
    return numbers


if __name__ == '__main__':
    print(sort_list_imperative([3, 6, 7, 9, 0, 100, 8, 1000]))
    print(sort_list_imperative_insert([3, 6, 7, 9, 0, 100, 8, 1000]))
    print(sort_list_declarative([3, 6, 7, 9, 0, 100, 8, 1000]))
    print(sort_list_declarative_insert([3, 6, 7, 9, 0, 100, 8, 1000]))
