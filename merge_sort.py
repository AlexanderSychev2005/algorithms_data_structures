# Merge Sort O(N log N) Implementation

# Merging two sorted lists into one
def merge_list(a, b):
    c = []
    N = len(a)
    M = len(b)

    i = 0
    j = 0

    while i < N and j < M:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]  # Append remaining elements if any exist
    return c


# Merge Sort function
def merge_sort_split_and_merge(A):
    N1 = len(A) // 2
    a1 = A[:N1]
    a2 = A[N1:]

    if len(a1) > 1:
        a1 = merge_sort_split_and_merge(a1)
    if len(a2) > 1:
        a2 = merge_sort_split_and_merge(a2)

    return merge_list(a1, a2)


a = [8, 2, 4, 9, 3]
sorted_a = merge_sort_split_and_merge(a)
print(sorted_a)
