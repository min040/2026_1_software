n = int(input())
cards = list(map(int, input().split()))

count = {}
for c in cards:
    count[c] = count.get(c, 0) + 1

m = int(input())
query = list(map(int, input().split()))

print(' '.join(str(count.get(q, 0)) for q in query))