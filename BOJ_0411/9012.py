t = int(input())

for _ in range(t):
    s = input()
    cnt = 0
    ok = True

    for ch in s:
        if ch == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            ok = False
            break

    if cnt != 0:
        ok = False

    print("YES" if ok else "NO")