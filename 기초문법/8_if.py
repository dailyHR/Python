# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 14:46:07 2022

@author: HR
"""

password = "A1234!"

user_input = input("비밀번호를 입력하세요.")

if user_input == password:
    print("잠금이 해제되었습니다.")
else :
    print("비밀번호를 잘못 입력하셨습니다.")

