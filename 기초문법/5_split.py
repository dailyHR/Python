# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 15:12:38 2022

@author: HR
"""

# 곱셈할 두 수를 입력받아서 결과 출력하기

a, b =input("곱셈할 두 수를 입력하세요. 예) 10 4").split()

# 스페이스로 구분된 2개의 숫자를 .split()을 사용하여 구분

print(int(a) * int(b))

print(f"두 수의 곱은 {int(a) * int(b)} 입니다.")
print(f"{int(a)} x {int(b)} = {int(a) * int(b)} ")
