t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    j = 1
    res = []
    while j < n:
        if (a[i] > 0 and a[j] < 0) or (a[i] < 0 and a[j] > 0):
            res.append(a[i])
            i = j
            j += 1
        else:
            if a[j] > a[i]:
                i = j
            j += 1
    res.append(a[i])
    print(sum(res))
