# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:56:36 2022

@author: fud37
"""

password = "fud37!"
user_input = input("!! 잠금 !! 비밀번호를 입력해 주세요. 입력까지 5회 남았습니다. >>> ")
check = 5

while user_input != password :
    if check == 0:
        print("입력 기회를 모두 사용하셨습니다.")
        break
    else :
        
        user_input = input(f"잘못된 비밀번호입니다. 다시 입력해 주세요. 입력까지 {check}회 남았습니다. >>> ")
        check -= 1
if check > 0 :
    print("!! 잠금이 해제되었습니다. !!")