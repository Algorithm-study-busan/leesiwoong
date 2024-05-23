class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: #
        def dfs(i,j):
            visited[i][j]=1
            
            for k in range(4):
                nx = j+dx[k]
                ny = i+dy[k]

                if 0<=nx<c and 0<=ny<r and grid[ny][nx]=='1' and not visited[ny][nx]:
                    dfs(ny,nx)
                    
        r, c = len(grid), len(grid[0])
        ans = 0
        visited = [[0] * c for _ in range(r)]
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]

        for i in range(r):
            for j in range(c):
                if grid[i][j]=='1' and not visited[i][j]:
                    dfs(i,j)
                    ans+=1
        return ans