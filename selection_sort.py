def selection_sort(A, i=None):
    """Sorts A[:i+1="""
    if i is None: i = len(A) - 1
    if i > 0:
        j = prefix_max(A, i)
        A[i], A[j] = A[j], A[i]
        selection_sort(A, i - 1)
    return A


def prefix_max(A, i):
    """Returns index of maximum element in A[:i+1] """
    if i > 0:
        j = prefix_max(A, i - 1)
        if A[i] < A[j]:
            return j
    return i


def selection_sort_video(A):
    n = len(A)

    for i in range(n - 1):
        m = A[i]  # minimum element
        p = i  # index of minimum element
        for j in range(i + 1, n):
            if A[j] < m:
                m = A[j]
                p = j

        if p != i:
            t = A[i]
            A[i] = A[p]
            A[p] = t
    return A


def selection_sort_video_rs(A):
    n = len(A)

    for i in range(n - 1):
        m = A[i]  # minimum element
        p = i  # index of minimum element
        for j in range(i + 1, n):
            if A[j] > m:
                m = A[j]
                p = j

        if p != i:
            t = A[i]
            A[i] = A[p]
            A[p] = t
    return A


def selection_sort_recitation(A):
    n = len(A)
    for i in range(n-1, 0, -1):
        m = i # index of maximum element
        for j in range(i):
            if A[j] > A[m]:
                m = j
        A[m], A[i] = A[i], A[m]
    return A


A = [8, 2, 4, 9, 3]

print(selection_sort(A, 4))
print(selection_sort_video(A))
print(selection_sort_video_rs(A))
print(selection_sort_recitation(A))
