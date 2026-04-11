k, l = map(int, input().split())

order = {}

for i in range(l):
    student = input()
    order[student] = i

res = sorted(order.items(), key=lambda x: x[1])

for i in range(min(k, len(res))):
    print(res[i][0])