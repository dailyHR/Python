# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:25:01 2022

@author: fud37
"""
import random
import time

playing = True
point = 0

start_time = time.time()

while playing :
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)
    num3 = random.randint(1,9)
    
    answer = num1 * num2 - num3
    
    user_input = int(input(f"{num1} * {num2} - {num3} = "))
    
    if user_input == answer :
        point += 1
        print(f"정답입니다. 현재 점수는 {point}입니다.")
    else :
        playing = False
        print(f"아쉽네요. 정답은 {answer}입니다.")
    
    
end_time = time.time()
second = end_time - start_time
print(f"총 {point}문제를 {round(second, 2)}초만에 해결하셨습니다!")
# round(반올림할 수, 나타낼 소수점 자리 수)