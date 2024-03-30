n, k = map(int,input().split())
jewels = list(map(int,input().split()) for _ in range(n))

dp = [0] * (k+1)

for weight, cost in jewels:
    for i in range(weight,k+1):
        dp[i] = max(dp[i],dp[i-weight]+cost)

print(max(dp))