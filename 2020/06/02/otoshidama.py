N, Y = map(int, input().split())
Y //= 1000
flag = False
for x in reversed(range(N + 1)):
    for y in reversed(range(N + 1 - x)):
        z = N - x - y
        if 10 * x + 5 * y + 1 * z == Y:
            print(x, y, z)
            flag = True
            break
    else:
        continue
    break

if not flag:
    print(-1, -1, -1)

