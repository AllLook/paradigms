#import sys
#print(sys.getrecursionlimit())
#sys.setrecursionlimit(2200)

numbers = [3, 8, 12, 9, 78, 6, 65, 7]
lst = sorted(numbers, reverse=True)


def binary_search_el(lst, value, min, max) -> int:
    if max < min:
        return -1
    else:
        midpoint = (min + max) // 2  # середина массива
        if lst[midpoint] < value:  # идем по правой  части если искомое больше середины
            return binary_search_el(lst, value, midpoint + 1,
                                    max)  # ищем смещаясь на один шаг смещаясь каждый раз когда условие выполняется
        elif lst[midpoint] > value:
            return binary_search_el(lst, value, min,
                                    midpoint - 1)  # ищем смещаясь на один шаг смещаясь каждый раз когда условие выполняется в другую сторону
        else:
            return midpoint  # сразу совпадение середины с искомым индексом элемента


if __name__ == '__main__':
    print(binary_search_el(lst, 9, 0, len(lst) - 1))
