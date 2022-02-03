# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 16:38:35 2022

@author: HR
"""

quiz = [
        ["gravity의 뜻은?", "산소", "위성", "중력", "윤리학", 3],
        ["satellite의 뜻은?", "은하계","실험실", "문화 충격", "위성" ,4],
        ["nutrient의 뜻은?" ,"영양소","윤리학","중력","위성", 1]
        ]

for i in range(0, len(quiz)) :
    print(f"문제 {i+1}번. {quiz[i][0]}")
    for j in range(1,5):
        print(f"{j}. {quiz[i][j]}")
    user_input = int(input("정답을 입력해주세요. >>> "))
    if(user_input == quiz[i][5]):
        print("정답입니다.")
    else :
        print(f"오답입니다. 정답은 {quiz[i][5]}번 입니다.")
