# O(N^2) Insertion Sort Implementation

def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
            else:
                break

    return A



ls = [-3, 5, 0, -8, 1, 10]
sorted_ls = insertion_sort(ls)
print(sorted_ls)

