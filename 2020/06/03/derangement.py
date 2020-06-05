N = int(input())
p = list(map(int, input().split()))
count = 0
i = 0
while i < N:
    if i+1 == p[i]:
        count += 1
        i += 1
    i += 1
print(count)

