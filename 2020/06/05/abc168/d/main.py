def solve():
        N, M = map(int, input().split())
        A = [[] for _ in range(N+1)]
        Q = [[] for _ in range(N+1)]
        print(A)
        for _ in range(M):
            a, b = map(int, input().split())
            A[a].append(b)
            A[b].append(a)
        q = [1]
        d = [0 for _ in range(N+1)]
        for v in q:
            for w in A[v]:
                print('v:', v,'w:', w)
                if d[w] < 1:
                    d[w] = v
                    q.append(w)
                    print(d)








        print(A)
        print(Q)



if __name__ == '__main__':
    solve()
