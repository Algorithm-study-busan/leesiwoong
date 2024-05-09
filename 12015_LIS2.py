import bisect

n=int(input())
arr= list(map(int,input().split()))

d= [] # 오름차순 시 i번째로 올수있는 가장 작은 수의 배열

for num in arr:
    lower_bound_idx = bisect.bisect_left(d, num)

    if lower_bound_idx == len(d):
        d.append(num)
    
    else:
        d[lower_bound_idx] = num

print(len(d))