# N, A, B = map(int, input().split())
# someSums = 0
# for i in range(1, N+1):
#     if A <= (i // 10000) % 10 + (i // 1000) % 10 + (i // 100) % 10 + (i // 10) % 10 + (i % 10) <= B:
#         someSums += i
# print(someSums)


n = 10
print(str(n))
print(sum(map(int, str(n))))
