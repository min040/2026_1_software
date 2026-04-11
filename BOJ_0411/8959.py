t = int(input())

for _ in range(t):
    s = input()
    score = 0
    cnt = 0

    for ch in s:
        if ch == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0

    print(score)