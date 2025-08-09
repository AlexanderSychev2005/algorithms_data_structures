# FIFO (First In, First Out) Queue Implementation

import collections

q = collections.deque()


def enqueue(q, item):
    q.append(item)
    print(f"Enqueued: {item}")


def dequeue(q):
    item = q.popleft() if q else None
    if item is not None:
        print(f"Dequeued: {item}")
        return item
    else:
        print("Queue is empty, nothing to dequeue.")


enqueue(q, 3)
enqueue(q, 5)

item = dequeue(q)
print(f"Dequeued item: {item}")

item = dequeue(q)
print(f"Dequeued item: {item}")

item = dequeue(q)
print(f"Dequeued item: {item}")