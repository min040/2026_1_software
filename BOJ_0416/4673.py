def d(n):
    return n + sum(map(int, str(n)))

nums = set(range(1, 10001))
gen = set()

for i in range(1, 10001):
    gen.add(d(i))

for x in sorted(nums - gen):
    print(x)