n = int(input())
k = int(input())

# 이진탐색 어려운 유형의 핵심
# 몇분안에 가능? => (x분안에 가능?) * n...

def bisect(target, s, e):
    while s<=e:
        mid = (s+e)//2

        cnt=0
        for i in range(1, n+1):
            cnt+= min(mid//i, n)
        # 값 // 행 == 행에서 값보다 작은 개수들
        # 근데 값>행이라면 애초에 그 개수는 행의 개수겠지?
        # 1 base indexing이라 개수가 곧 인덱스

        if cnt>=target:
            e = mid-1
        elif cnt<target:
            s = mid+1
        # cnt==target일때 cnt == mid의 idx == k 이니 return mid 아닌가?
        # 

    return s

print(bisect(k,1, n*n))