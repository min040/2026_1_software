n = int(input())

def is_hansu(x):
    s = str(x)
    if len(s) <= 2:
        return True
    d = int(s[1]) - int(s[0])
    for i in range(1, len(s)-1):
        if int(s[i+1]) - int(s[i]) != d:
            return False
    return True

print(sum(1 for i in range(1, n+1) if is_hansu(i)))