import math

n = int(input())

chae = [0,0] + [1] * (n-1)
for i in range(2, int(n**0.5)+1):
    if chae[i]==1:
        for j in range(i*i, n+1, i):
            chae[j]= 0

sosu = [i for i in range(2, n+1) if chae[i] == 1]

l,r = 0,0
cnt =0

while r<=len(sosu):
    tmp = sum(sosu[l:r])
    if tmp == n:
        cnt+=1
        r+=1
    elif tmp<n:
        r+=1
    else:
        l+=1

print(cnt)
