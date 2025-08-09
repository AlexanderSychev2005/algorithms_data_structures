# QuickSort using Hoare's partition scheme O(N log N) average case

import random


def quick_sort(a: list) -> list:
    if len(a) > 1:
        x = a[random.randint(0, len(a) - 1)]  # Choose a random value as pivot
        low = [i for i in a if i < x]
        eq = [i for i in a if i == x]
        high = [i for i in a if i > x]
        a = quick_sort(low) + eq + quick_sort(high)
    return a


a = [8, 2, 4, 9, 3]
sorted_a = quick_sort(a)
print(sorted_a)
