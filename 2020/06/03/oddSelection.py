t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    evenk = 0
    oddk = 0
    for i in range(n):
        if (a[i] % 2 == 0):
            evenk += 1
        else:
            oddk += 1
    for i in range(1, oddk + 1, 2):
        if evenk >= (x - i) and i <= x:
            print('Yes')
            break
        else:
            print('No')
