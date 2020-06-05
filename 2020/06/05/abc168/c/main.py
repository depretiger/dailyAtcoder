import math


def solve():
    A, B, H, M = map(int, input().split())
    theta = abs((H+(M/60))*30-M*6)
    x = abs(math.sqrt(A**2+B**2-2*A*B*math.cos(math.radians(theta))))
    print(x)


if __name__ == '__main__':
    solve()
