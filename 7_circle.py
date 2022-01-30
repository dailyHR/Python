# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 14:39:37 2022

@author: HR
"""

r = float(input("반지름을 입력해 주세요.\n"))

print(f"원의 넓이 : {round(r*r*3.14,2)}")
print(f"원의 둘레 : {r*2*3.14}")
print(f"원의 넓이(거듭제곱 사용) : {r**2 * 3.14}")

# 거듭제곱 사용 : a ** b
# 반올림 : round(반올림할 수, 나타낼 소수점 자리 수)