s = input()
t = input()
# ss = ''.join(sorted(list(s)))
# st = ''.join(sorted(list(t),reverse=True))
ss = sorted(s)
st = sorted(t)
# print('YNeos'[ss >= st::2])
print(ss >= st)
