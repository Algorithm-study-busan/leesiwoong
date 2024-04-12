n,k = map(int,input().split()) # n종류 동전으로 k원을 최소개수로 구현

units = [int(input()) for _ in range(n)]
cnt=0

for i in range(len(units)-1, -1,-1):
    if k-units[i]<0 : continue

    
    cnt += k // units[i] # 동전개수는 k / unit의 몫
    k %=units[i] # 나머지금액은 나머지연산
print(cnt)