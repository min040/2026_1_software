n = int(input())
x = list(map(int, input().split()))

x.sort()

prefix = 0
answer = 0

for i in range(n):
    answer += x[i] * i - prefix
    prefix += x[i]

print(answer)