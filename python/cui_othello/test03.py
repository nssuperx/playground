# -*- coding:utf-8 -*-

a = [[0 for i in range(9)] for i in range(9)]

for i in range(9):
    for j in range(9):
        a[i][j] = i * j

for i in range(9):
    a[0][i] = i

for i in range(9):
    a[i][0] = i

for i in range(9):
    for j in range(9):
        print("{0:>3}".format(a[i][j]),end="")
    print()
        
#print(a)
