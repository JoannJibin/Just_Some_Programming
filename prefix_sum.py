#prefix sum concept
#question: give Range sum for given queries

n,q = map(int,input().split())
k = list(map(int,input().split()))
prefix_sum = []
p_sum = 0

for i in range(n):
    p_sum += k[i]
    prefix_sum.append(p_sum)

for i in range(q):
    start,end = map(int,input().split())
    if start-1 == 0:
        print(prefix_sum[end-1])
    else:
        print(prefix_sum[end-1] - prefix_sum[start-2])
