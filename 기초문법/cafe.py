# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 13:49:15 2022

@author: fud37
"""

menu = 0
flavor = ['사과', '토마토', '키위', '망고']

while menu != 5 :
    
    print(""" 
          == 주스 카페 관리자 모드 ==
          ==== 관리자 모드 ====
          1. 메뉴보기
          2. 신메뉴 추가하기
          3. 메뉴 삭제하기
          4. 메뉴 이름 바꾸기
          5. 관리자 모드 종료하기
          """)
    menu = int(input("원하는 기능을 선택하세요. >>> "))
    
    # 1. 메뉴보기
    
    if menu == 1 :
        print("=== 메뉴 ===")
        
        # 1.인덱스 사용
        # for i in range(0, len(flavor)) :
        #     print(f"{flavor[i]} 주스")
        
        # 2. in 리스트 사용
        for i in flavor :
            print(f"{i} 주스")
            
    elif menu == 2 :
        new_flavor = input("메뉴 이름을 입력해 주세요.")
        flavor.append(new_flavor)
        # 리스트명.append(변수)로 리스트에 추가
    elif menu == 3 :
        remove_flavor = input("삭제할 메뉴이름을 입력해주세요.")
        flavor.remove(remove_flavor)
        # 리스트명.remove(삭제하고싶은 변수)로 리스트에서 삭제 
    elif menu == 4:
        for i in range(0, len(flavor)):
            print(f"{i}. {flavor[i]}")
        index = int(input("몇 번째 메뉴를 변경할까요? "))
        change_flavor = input("변경할 메뉴 이름을 입력해주세요.")
        flavor[index] = change_flavor
    else :
        print("관리자 모드를 종료합니다.")
        break