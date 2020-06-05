# def solve():
#     N = int(input())
#     t = [0] * (N+1)
#     x = [0] * (N+1)
#     y = [0] * (N+1)
#     t[0] = 0
#     x[0] = 0
#     y[0] = 0
#     for i in range(1, N+1):
#         t[i], x[i], y[i] = map(int, input().split())
#         # 空間的に可能かどうか。奇数秒後はx+yが奇数に、偶数秒後はx+yが偶数にならないといけない。
#         if (t[i]%2==0 and (x[i]+y[i])%2==1) or (t[i]%2==1 and (x[i]+y[i])%2==0):
#             print('No')
#             exit()
#         #　時間的に可能かどうか。
#         if (t[i] - t[i-1]) < abs(x[i] - x[i-1]) + abs(y[i] - y[i-1]):
#             print('No')
#             exit()
#     print('Yes')
#
#
# if __name__ == '__main__':
#     solve()


def solve():
    N = int(input())
    t_p = 0
    x_p = 0
    y_p = 0
    for i in range(1, N+1):
        t, x, y = map(int, input().split())
        #　時間的に可能かどうか。
        if (t - t_p) < abs(x - x_p) + abs(y - y_p):
            print('No')
            exit()
        # 空間的に可能かどうか。奇数秒後はx+yが奇数に、偶数秒後はx+yが偶数にならないといけない。
        if (t%2==0 and (x+y)%2==1) or (t%2==1 and (x+y)%2==0):
            print('No')
            exit()
        t_p, x_p, y_p = t, x, y
    print('Yes')


if __name__ == '__main__':
    solve()

