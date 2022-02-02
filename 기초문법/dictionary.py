# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 14:10:06 2022

@author: fud37
"""

# 딕셔너리 : 인덱스 대신 각 값마다 키를 사용해서 이름을 붙여줌
# 리스트는 [], 딕셔너리는 {}를 사용한다.
# 키와 값은 : 으로 구분 ex) {키1:값1, 키2:값2}

dict_eng = {"apple" : "사과", "peach":"복숭아" ,"mango" : "망고"}
user_input = input("검색할 영어 단어를 입력하세요 >>> ")

while user_input != "종료" :
        
    if user_input in dict_eng :
        print(f"검색하신 {user_input}의 뜻은 {dict_eng[user_input]}입니다.")
    else :
        print("검색하신 단어는 등록되어 있지 않습니다.")
    user_input = input("검색할 영어 단어를 입력하세요 >>> ")


# if 문에 in 딕셔너리 표현
# 딕셔너리 내에 user_input의 값이 존재하면 True를 반환, 그렇지 않으면 False 반환
