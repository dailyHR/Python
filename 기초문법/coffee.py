# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 13:23:21 2022

@author: fud37
"""
import random
import time

print("!! 커피 값 내기 !! 오늘은 누가 커피를 사게 될까요?")

name= input("참가자들의 이름을 입력해 주세요. 예) 철수 영희 >>> ").split()
# split으로 분리시켜 name에 저장. 리스트 형식으로 저장됨.

number_of_people = len(name);
# 리스트에 담긴 데이터 수 확인 : len(리스트명)

print(f"총 {number_of_people}명 참가하셨습니다.")

winner = random.choice(name)
# random.choice(리스트명) : 리스트 내의 항목을 랜덤으로 추출

print("오늘 선택된 사람은.... ")
time.sleep(3)
# 시간 지연 -> time.sleep(초)로 지연시킬 수 있음

print(f"{winner} 입니다!")