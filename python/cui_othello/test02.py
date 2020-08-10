# -*- coding:utf-8 -*-

def twothree(num):
    if num % 2 == 0 and num % 3 == 0:
        print(num,'は6の倍数です')
    elif num % 3 == 0:
        print(num,'は3の倍数です')
    elif num % 2 == 0:
        print(num,'は2の倍数です')
    else:
        print(num,'は2と3の倍数ではないです')

print('2の倍数か3の倍数か')
twothree(int(input()))
