# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 14:51:39 2022

@author: HR
"""

name = input("이름을 적어주세요.")
print(name + "님 안녕하세요.")

print("사과 1개 : 500원")
count = int(input("사과 몇개를 드릴까요?"))
# input으로 들어오는 값은 모두 문자형태.
# 따라서 int로 변환을 해주어야함.

print("총 금액은", 500 * count,"원 입니다.")
print(f"총 금액은 {500*count}원 입니다.")
