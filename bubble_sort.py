# O (N^2) Bubble Sort Implementation

def bubble_sort_f(ls):
    n = len(ls)
    for i in range(n):  # n - 1 iterations
        for j in range(n - 1 - i):  # last not sorted elements
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls

def bubble_sort_f_rs(ls):
    n = len(ls)
    for i in range(n):  # n - 1 iterations
        for j in range(n - 1 - i):  # last not sorted elements
            if ls[j] < ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls



ls = [7, 5, -8, 0, 10, 1]
sorted_ls = bubble_sort_f(ls)
print(sorted_ls)

reversed_sorted_ls = bubble_sort_f_rs(ls)
print(reversed_sorted_ls)
