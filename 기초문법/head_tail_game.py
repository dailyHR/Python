# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:52:07 2022

@author: fud37
"""

import random

print("동전 던지기 게임에 오신 것을 환영합니다.")

keep_playing = "yes"

while keep_playing == "yes" :
    
    choice = int(input("앞면일까요? 뒷면일까요? 0:앞면 1:뒷면 \n"))
    
    # random.randint(0,10) -> 특정 정수 범위 내에서 무작위 값 추출
    coin = random.randint(0,1)
    
    print(f"나의 선택 : {choice}")
    print(f"컴퓨터의 선택 : {coin}")
    
    if coin == choice :
        print("정답!")
    else :
        print("틀렸음!")
    
    keep_playing = input("계속하시겠습니까? yes or no >>> ").lower()