def mult_table(n):
    i = 1
    j = 1
    while j <= n:
        temp = i * j
        print(f"{i} * {j} = {temp}")
        j += 1


def mult_table_double(n):
    j = 1
    for i in range(1, n + 1):
        temp = j * i
        print(f"{j} * {i} = {temp}")


if __name__ == '__main__':
    mult_table(9)
    mult_table_double(9)
