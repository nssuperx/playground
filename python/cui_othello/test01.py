# -*- coding:utf-8 -*-

print('あああああ')

num = input()

if(num == '5'):
  print(num)
else:
  print('not 5')

try:
  a = int(num)
  print(a)
except ValueError:
  print("int only")

      
