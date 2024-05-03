n = int(input())

arr = list(map(int,input().split()))

stack = []

receive_num = 1

# arr도 큐처럼 써서 두개 관리했는데 굳이 그럴필요없었음
for i in arr:
    stack.append(i)

    while stack and stack[-1] == receive_num:
        stack.pop()
        receive_num+=1 
        # pop되고 새로된 top이 +1된 수령대상일 수도 있으니 반복

print('Sad') if stack else print("Nice")