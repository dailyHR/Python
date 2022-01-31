# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 14:34:35 2022

@author: HR
"""

print("지금부터 타이머를 누르고 문제를 풀어보세요")
second = int(input("몇 초만에 문제를 해결하셨나요?"))
# minute = int(second / 60)
minute = second // 60
# 몫은 a // b로 구할 수 있음
second2 = second % 60

print(f"{minute}분 {second2}초만에 문제를 해결하셨군요")
