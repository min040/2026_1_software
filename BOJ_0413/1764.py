n, m = map(int, input().split())

a = set(input() for _ in range(n))
b = set(input() for _ in range(m))

res = sorted(a & b)

print(len(res))
for x in res:
    print(x)