class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        from collections import deque

        n = len(board)
        visited = [0]*(n**2 +1)

        def getCoordinate(cell):
            r,c = divmod(cell-1, n) 
            # 1 base idx라 cell-1해야 인덱스 조정됨
            c = (n-1)-c if r%2==1 else c
            r = (n-1)-r

            return r,c

        q = deque([[1,0]])
        visited[1] = 1

        while q:
            cell, cnt = q.popleft()
            for i in range(1, 6+1):
                next = cell + i
                r,c = getCoordinate(next)
                
                if board[r][c] !=-1:
                    next = board[r][c]
                
                if next == n*n: return cnt+1

                if not visited[next]: # n*n보다 작은지 검사는 불필요. 어차피 그전에 n*n에서 걸러졌음
                    q.append([next, cnt+1])
                    visited[next] = 1
        return -1


