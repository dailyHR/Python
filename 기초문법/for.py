# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:37:06 2022

@author: fud37
"""

# for문 -> range()함수와 자주 사용
# range(a, b) -> a이상 b미만

sum_100 = 0

for i in range(1,101) :
    sum_100 += i

print(sum_100)

# range()함수에 3번째 매개변수 : 변수만큼씩 건너뜀

sum_even = 0
for i in range(0, 101, 2):
    sum_even += i

print(sum_even)