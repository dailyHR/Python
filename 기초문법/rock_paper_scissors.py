# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 13:35:20 2022

@author: fud37
"""

import random

user_input = int(input("0: 바위, 1: 가위, 2: 보 >>> "))

print(f"나의 선택 : {user_input}")
rps_list = [0,1,2]
# random.rnadint(0,2)
computer_choice = random.choice(rps_list)

print(f"컴퓨터 선택 : {computer_choice}")

""" 내가 짠 코드
if user_input == 0 :
    if computer_choice == 1 :
        print("이겼습니다.")
    elif computer_choice == 2 :
        print("졌습니다.")
    else : 
        print("비겼습니다.")
elif user_input == 1 :
    if computer_choice == 0 :
        print("졌습니다.")
    elif computer_choice == 1 :
        print("비겼습니다.")
    else :
        print("이겼습니다.")
else :
    if computer_choice == 0 :
        print("이겼습니다.")
    elif computer_choice == 1:
        print("졌습니다.")
    else :
        print("비겼습니다.")
"""

if computer_choice == user_input :
    print("비겼습니다.")
elif (user_input - computer_choice == -1) or (user_input == 2 and computer_choice == 0) :
    print("이겼습니다.")
else :
    print("졌습니다.")