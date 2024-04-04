import sys; sys.stdin = open("i.txt",'r')

n = int(input())
times = list(map(int,input().split()))

times.sort()
waiting_time = [0] * n

for i in range(n):
    waiting_time[i] += times[i] + waiting_time[i-1]

print(sum(waiting_time))

# max(times)를 모두가 기다릴 필요는 없다!
