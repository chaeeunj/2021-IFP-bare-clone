''' 표준 입력으로 가격(정수)과 쿠폰 이름이 각 줄에 입력됩니다. 
Cash3000 쿠폰은 3,000원, Cash5000 쿠폰은 5,000원을 할인합니다. 
쿠폰에 따라 할인된 가격을 출력하는 프로그램을 만드세요
(input에서 안내 문자열은 출력하지 않아야 합니다) '''

price = int(input())
coupon = input()
if coupon == 'Cash3000' :
    print(price - 3000)
if coupon == 'Cash5000' :
    print(price - 5000);