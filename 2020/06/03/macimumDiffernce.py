# N = input()
# A = sorted(map(int, input().split()))
# print(A[-1] - A[0])
N = input()
A = list(map(int, input().split()))
print(max(A) - min(A))
