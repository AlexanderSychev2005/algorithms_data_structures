# Binary Search Implementation in Python, O(log N)

def binary_search_f(ls, value):
    n = len(ls)

    left, right = 0, n-1

    while left <= right:
        middle = (left + right) // 2
        v = ls[middle]

        if v == value:
            return v, middle
        elif v < value:
            left = middle + 1
        else:
            right = middle - 1
    return None, -1  # Value not found


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

value = 5

result, index = binary_search_f(nums, value)
print(f"Value {value} found at index {index}" if index != -1 else f"Value {value} not found")