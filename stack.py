# LIFO (Last In, First Out) stack implementation

a = input("Enter the string of the elements: ")
stack = []
flVerify = True

for i in a:
    if i in "([{":
        stack.append(i)
    elif i in ")]}":
        if len(stack) == 0:
            flVerify = False
            break

        br = stack.pop()
        if i == '(' and br != ')':
            continue
        if i == '[' and br != ']':
            continue
        if i == '{' and br != '}':
            continue

        flVerify = False
        break

if flVerify and len(stack) == 0:
    print("Yes")
else:
    print("No")