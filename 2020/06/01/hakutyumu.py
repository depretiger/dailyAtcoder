# S = input()
# while len(S) > 0:
#     if S[-5::1] == 'dream' or S[-5::1] == 'erase':
#         S = S[:-5:1]
#     elif S[-6::1] == 'eraser':
#         S = S[:-6:1]
#     elif S[-7::1] == 'dreamer':
#         S = S[:-7:1]
#     else:
#         print('NO')
#         break
#
# if len(S) == 0:
#     print('YES')


S = input().replace('eraser', '!').replace('erase', '!').replace('dreamer', '!').replace('dream', '!').replace('!', '')
if len(S) == 0:
    print('YES')
else:
    print('NO')

