N = int(input())

dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

res = dist[0] * cost[0]
min_cost = cost[0]

for i in range(1, N - 1):
    if(min_cost > cost[i]):
        min_cost = cost[i]
    res += min_cost * dist[i]
    
print(res)
