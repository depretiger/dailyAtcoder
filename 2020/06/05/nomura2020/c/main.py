def solve():
    T = list(input())
    print(T)
    while len(T) > 0:
        T.pop(-1)
        print(T)


if __name__ == '__main__':
    solve()
