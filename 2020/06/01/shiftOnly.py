# N = int(input())
# A = list(map(int, input().split()))
# even = lambda x: True if x % 2 == 0 else False
# div2 = lambda x: x/2
# isContinue = True
# c = 0
# while isContinue:
#     for i, v in enumerate(A):
#         if even(v):
#             A[i] = div2(v)
#         else:
#             isContinue = False
#     if isContinue:
#         c += 1
# print(c)
#
#
#
#
#
input()
n = eval(input().replace(' ', '|'))
print(len(bin(n & -n)) - 3)

