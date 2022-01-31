# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 16:59:07 2022

@author: HR
"""

print("-메뉴-")

print("1. 아메리카노 1,800원")
print("2. 카페라떼 2,600원")
print("3. 핫초코 2,300원")

menu = int(input("커피 종류를 선택하세요. 번호 입력 >>> "))
if menu > 3 or menu < 1 :
    print("잘못된 입력입니다. 다시 확인해주세요.")
else :
    num = int(input("몇 잔을 드릴까요? >>> "))
    if num < 0:
        print("잘못된 입력입니다. 다시 확인해주세요.")
    else :
        price = 0
        if menu == 1 :
            price = 1_800
        elif menu == 2:
            price = 2_600
        else :
            price = 2_300
            
        price = price * num
        money = int(input(f"총 금액은 {price}원 입니다. 돈을 투입해 주세요 >>> "))
        
        if money >= price :
            print(f"{money}원을 받았습니다. 거스름돈은 {money - price}원입니다.")
            return_money = money - price
            num_1000 = return_money // 1000
            return_money = return_money % 1000
            num_500 = return_money // 500
            return_money = return_money % 500
            num_100 = return_money //100
            print(f"1000원 지폐 {num_1000}장, 500원 동전 {num_500}개, 100원 동전 {num_100}개")
        else :
            print("금액이 부족합니다. 주문이 취소되었습니다.")
