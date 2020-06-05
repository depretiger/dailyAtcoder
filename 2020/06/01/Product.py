# -*- coding: utf-8 -*-
# スペース区切りの整数の入力
a, b = map(int, input().split())
if a * b % 2 == 1:
    print("Odd")
else:
    print("Even")
