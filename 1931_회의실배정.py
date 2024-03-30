n = int(input())
meetings = [list(map(int,input().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))
# 회의 종료시각이 가장 빠른 회의 찾고
# 그 시점 기준 회의 시작시각이 가장 빠른 회의를 찾아 잇기

cnt = prev_endtime = 0
for s,e in meetings:
    # 현재 종료시각으로부터 가장 빠른 시작시간 찾기
    if s >= prev_endtime:
        # 찾았다면 카운트 증가하고 종료시각 갱신
        cnt += 1
        prev_endtime = e

print(cnt)