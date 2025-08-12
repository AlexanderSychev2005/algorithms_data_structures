marks = [2, 2, 3, 4]
lst = [True, "True", 1, 1.0]

print(len(marks))

lst.append(5)  # O(1)
print(lst)

lst.insert(0, "First")  # O(N)
print(lst)

print(marks[0])  # O(1)
marks[0] = 5  # O(1)
print(marks)

print(marks + lst)  # O(N + M)
print(marks[1:3])  # O(N)
