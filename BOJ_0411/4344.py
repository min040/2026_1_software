t = int(input())

for _ in range(t):
    data = list(map(int, input().split()))
    n = data[0]
    scores = data[1:]

    avg = sum(scores) / n
    count = sum(1 for x in scores if x > avg)

    print(f"{count/n*100:.3f}%")