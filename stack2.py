# stack = []
#
# stack.append(1)
# stack.append(2)
#
# value = stack.pop()
# print(f"Popped value: {value}")

from collections import deque
from queue import LifoQueue

stack = deque([1, 2, 3, 4, 5])

# stack.append(6)
# stack.append(7)
#
# value = stack.pop()

stack.appendleft(0)
stack.appendleft(-1)

value = stack.popleft()
print(f"Popped value: {value}")
print(stack)