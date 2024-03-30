import sys
sys.stdin = open("input.txt",'r')

m = [list(map(int,input().split())) for _ in range(9)]

maxval = -1

for i in range(9):
    for j in range(9):
        if m[i][j] > maxval:
            maxval = m[i][j]
            p,q = i, j

print(maxval)
print(p+1,q+1)