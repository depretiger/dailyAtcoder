def solve():
    T = list(input())
    x = 0
    while len(T) > 0:
        x += T[::2].count('1')
        if '0' in T[::2]:
            T[::-1].remove('0')
        else:
            del T[-1]
    print(x)

if __name__ == '__main__':
    solve()
