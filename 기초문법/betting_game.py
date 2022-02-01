# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:37:27 2022

@author: fud37
"""
import random

money = int(input("배팅 금액을 입력하세요. 단위: $ >>> "))
print(f"총 ${money} 배팅하셨습니다.")

road = int(input("3갈래의 길로 나뉘어 있습니다. 어느 길을 선택하시겠습니까? 1,2,3 >>> "))

answer = random.randint(1,3)
if answer == road :
    print(f"축하합니다! 배팅에 성공하셨습니다. 총 금액은 {money * 2}$가 되었습니다.")
    y_or_n = input("다음 단계로 이동하시겠습니까? 성공시 2배, 실패시 $0 y or n >>> ").lower()
    # lower는 소문자로 바꿔주는 함수
    if y_or_n == 'y' :
        print("다음 단계로 이동합니다.")
        door = int(input("3개의 문이 있습니다. 하나를 선택해주세요. 1,2,3 >>> "))
        answer = random.randint(1,3)
        if answer == door :
            print(f"축하합니다! 배팅에 성공하셨습니다. 총 금액은 f{money *2}$가 되었습니다.")
        else :
            money = 0
            print("아쉽네요. 모든 배팅 금액을 잃었습니다.")
    else :
        print(f"게임이 종료되었습니다. 총 금액은 {money *2}$입니다.")
else :
    print("틀렸습니다.")