# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 14:27:34 2022

@author: fud37
"""

quiz = [
        ["리스트 형식에서 데이터를 추가하는 방법은?","append"],
        ["리스트 형식에서 데이터를 삭제하는 방법은?", "remove"],
        ["파이썬에서 리스트 선언 방법은?", "[]"],
        ["튜플에서 데이터를 삭제할 수 있다? 없다?", "없다"]
        ]

point = 0
for x,y in quiz :
    print(x)
    user_input = input()
    
    if user_input == y :
        point += 1
        print(f"정답입니다. 현재 포인트는 {point}점 입니다.")
    else :
        print(f"틀렸습니다. 정답은 {y} 입니다.")