# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:41:18 2022

@author: fud37
"""


playing = "아니오"

while playing == "아니오" :
    dan = int(input("구구단 몇 단을 출력해 드릴까요? >>> "))

    for i in range(1,10) :
        print(f"{dan} x {i} = {dan * i}")
    
    playing = input("프로그램을 종료하시겠습니까? >>> ")