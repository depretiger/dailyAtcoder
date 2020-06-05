def solve():
    N = int(input())
    T, A = map(int, input().split())
    H = map(int, input().split())
    ans = float('inf')
    ans_i = 0
    for i, v in enumerate(H):
        tmp = abs(A - (T - 0.006 * v))
        if ans > tmp:
            ans_i = i
            ans = tmp
    print(ans_i+1)

if __name__ == '__main__':
    solve()
