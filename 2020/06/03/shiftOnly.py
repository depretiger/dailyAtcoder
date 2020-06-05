N = input()
n = eval(input().replace(' ', '|'))
print(len(str(bin(n&-n))[3:]))
