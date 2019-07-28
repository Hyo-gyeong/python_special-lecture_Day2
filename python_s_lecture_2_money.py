'''
#복습하기! 따라적었음!

#변수선언
money, c500, c100, c50, c10 = 0,0,0,0,0


#메인코드부분
money = int(input("교환할 돈은 얼마?"))

c500 = money // 500

money %= 500

c100 = money // 100

money %= 100

c50 = money // 50

money %= 50

c10 = money // 10

money %= 10

print("500원 %d장,100원 %d장,50원 %d장, 10원 %d장" % (c500, c100, c50, c10))

'''

'''
money, c50000, c10000, c5000, c1000, c500, c100, c50, c10 = 0,0,0,0,0,0,0,0,0

money = int(input("교환할 돈은 얼마?"))

c50000 = money // 50000

money %= 50000

c10000 = money // 10000

money %= 10000

c5000 = money // 5000

money %= 5000

c1000 = money // 1000

money %= 1000

c500 = money // 500

money %= 500

c100 = money // 100

money %= 100

c50 = money // 50

money %= 50

c10 = money // 10

money %= 10

rest = money // 1

print("50000원 %d장, 10000원 %d장, 5000원 %d장, 1000원 %d장, \n500원 %d장,100원 %d장,50원 %d장, 10원 %d장" % \
(c50000, c10000, c5000, c1000, c500, c100, c50, c10))
print("교환하지 못한 돈 %d원" % rest)

'''
'''
money = int(input("투입한 돈:"))
price = int(input("물건 값:"))
change = money - price
print("거스름 돈 %d" % change)

c500 = change // 500 #change를가지고 나눠야된다는거 주의! money를 나누면 안돼!

change %= 500

c100 = change // 100

change %= 100

print("500원 동전의 개수: " , c500)
print("100원 동전의 개수: " , c100)#이렇게 표현할 수도 있음
'''
