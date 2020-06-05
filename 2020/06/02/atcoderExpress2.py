# def solve():
#     N, M, Q = map(int, input().split())
#     L = [0] * M
#     R = [0] * M
#     p = [0] * Q
#     q = [0] * Q
#     for i in range(M):
#         L[i], R[i] = map(int, input().split())
#     for i in range(Q):
#         p[i], q[i] = map(int, input().split())
#     for i in range(Q):
#         c = 0
#         for j in range(M):
#             if p[i] <= L[j] and R[j] <= q[i]:
#                 c += 1
#         print(c)
# def solve():
#     N, M, Q = map(int, input().split())
#     LR = [0] * M
#     pq = [{}] * Q
#     for i in range(M):
#         LR[i] = set(map(int, input().split()))
#     for i in range(Q):
#         p, q = map(int, input().split())
#         pq[i] = set(range(p, q + 1))
#
#     for i in range(Q):
#         c = 0
#         for j in range(M):
#             if LR[j].issubset(pq[i]):
#                 c += 1
#         print(c)



# def solve():
#     N, M, Q, *x = map(int, open(0).read().split())
#     LR, pq = x[:2*M], x[2*M:]
#
#     mat = [[0] * (N + 1) for _ in range(N + 1)]
#     c = [[0] * (N + 1) for _ in range(N + 1)]
#     # ここでマトリックス作ってる
#     for l, r in zip(*[iter(LR)] * 2):
#         mat[l][r] += 1
#     # 累積和のためのマトリックス作成
#     for l in range(N+1):
#         for r in range(N+1):
#             for k in range(r+1):
#                 c[l][r] += mat[l][k]
#     # S計算
#     for p, q in zip(*[iter(pq)] * 2):
#         ans = 0
#         for l in range(p,q+1):
#             ans += c[l][q] - c[l][p-1]
#         print(ans)

#         print(ans)


from itertools import accumulate


def solve():
    N, M, Q, *x = map(int, open(0).read().split())
    LR, pq = x[:2*M], x[2*M:]

    mat = [[0] * (N + 1) for _ in range(N + 1)]
    c = [[0] * (N + 1) for _ in range(N + 1)]
    # ここでマトリックス作ってる
    for l, r in zip(*[iter(LR)] * 2):
        mat[l][r] += 1
    # 累積和のためのマトリックス
    for l in range(N+1):
        c[l] = list(accumulate(mat[l][:r+1]))
    # S計算
    for p, q in zip(*[iter(pq)] * 2):
        ans = 0
        for l in range(p, q+1):
            ans += c[l][q] - c[l][p-1]
        print(ans)


if __name__ == '__main__':
    solve()
