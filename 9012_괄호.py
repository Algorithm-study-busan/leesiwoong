T = int(input())

for _ in range(T):
    stack = []
    string = input()

    isVPS = 'NO'
    for c in string:
        if c == '(': stack.append(1)

        elif c == ')':
            if stack: stack.pop()
            else:
                isVPS = 'NO'
                break
    else: 
        if not stack: isVPS = 'YES'

    print(isVPS)