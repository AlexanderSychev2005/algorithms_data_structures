# FIFO (First In, First Out) Queue Implementation

import collections


# dq = collections.deque([1, 2, 3, 4, 5], maxlen=5)
# dq.append(6)  # The oldest item is removed
# print(dq)
# dq.appendleft(0)  # The oldest item is removed
# print(dq)
# dq.pop()
# print(dq)
# dq.popleft()
# print(dq)
#
# dq = collections.deque()
# try:
#     dq.pop()
# except IndexError as e:
#     print(e)

# dq = collections.deque([1, 2, 3, 4, 5])
# dq.extend([6, 7, 8])
# dq.extendleft([0, -1, -2])
# dq.insert(0, 100)
# dq.insert(100, 100)
# print(dq)
# dq.remove(100)
# print(dq)
# dq.clear()
# print(dq)
#
# dq2 = dq.copy()

# FIFO (First In, First Out) Queue Implementation
dq = collections.deque([1, 2, 3, 4, 5])
dq.appendleft(10)
value = dq.pop()

dq.append(10)
value = dq.popleft()

# LIFO (Last In, First Out) Stack Implementation
dq.append(10)
value = dq.pop()

dq.appendleft(10)
value = dq.popleft()

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
