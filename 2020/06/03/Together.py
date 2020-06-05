N = input()
a = map(int, input().split())
count = {}
for v in a:
    for i in [v-1, v, v+1]:
        if i in count.keys():
            count[i] += 1
        else:
            count[i] = 1

print(max(count.values()))
