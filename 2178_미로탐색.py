import sys;sys.stdin=open('input.txt','r')

from collections import deque

R,C = map(int,input().split())

miro =  [[i for i in input()] for _ in range(R)]
visited = [[0]*C for _ in range(R)]


def bfs():    
    q = deque([[0,0,1]])
    visited[0][0]=1

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    while q:
        r,c,cnt = q.popleft()

        if r == R-1 and c == C-1:
            return cnt
        
        for k in range(4):
            nx = c + dx[k]
            ny = r + dy[k]

            if 0<=nx<C and 0<=ny<R and miro[ny][nx]=='1' and not visited[ny][nx]:
                q.append([ny,nx,cnt+1])
                visited[ny][nx] = 1

print(bfs())



