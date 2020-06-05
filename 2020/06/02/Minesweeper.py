# def open_matrix(h,w,l_2d):
#     for i in range(h):
#         for j in range(w):
#             print(l_2d[i][j], end='')
#         print('\n',end='')
#
#
# H, W = map(int, input().split())
# S = [input() for _ in range(H)]
# newS = [[0 for _ in range(W)] for _ in range(H)]
# for i in range(H):
#     for j in range(W):
#         if S[i][j] == '.':
#             counter = 0
#             for k in [-1,0,1]:
#                 for l in [-1,0,1]:
#                     if 0 <= i+k < H and 0 <= j+l <W:
#                         if S[i+k][j+l] == '#':
#                             counter += 1
#             newS[i][j] = counter
#         else:
#             newS[i][j] = '#'
# open_matrix(H,W,newS)


