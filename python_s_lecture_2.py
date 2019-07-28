
'''
a = 200

if a < 100:
    print("100보다 작군요.")
print("거짓이므로 이 문장은 안 보이겠죠?")

print("프로그램 끝")
'''

'''
years = int(input("연도를 입력하세요."))

if (years % 4 == 0 and years % 100 != 0  or  years % 400 == 0):
    print("%d년은 윤년입니다."% years)
else:
    print(years,"년은 윤년이 아닙니다.") #이렇게 사용할 수도 있음.
'''

'''
a = 75

if a > 50:
    if a < 100:
        print("50보다 크고 100보다 작군요")
    else:
        print("100보다 크군요")
else:
    print("50이하의 수 이군요")
'''


'''
import random

print("동전 던지기 게임을 시작합니다.")

coin = random.randrange(2)

if coin == 0:
    print("동전의 뒷면이군요.")
else:
    print("동전의 앞면이군요.")
print("게임이 종료되었습니다.")
'''

'''
num = int(input("정수를 입력하세요."))

if num > 0 :
    print("양수입니다.")
elif num == 0 :
    print("양수도 음수도 아닌 0입니다.")
elif num < 0 :
    print("음수입니다.")
'''

'''
import random

diceA = random.randrange(1,7)
diceB = random.randrange(1,7)

print("A의 주사위 숫자는 %d입니다." % diceA)
print("B의 주사위 숫자는 %d입니다." % diceB)

if diceA >= diceB:
    if diceA == diceB:
        print("비겼습니다.")
    else:
        print("A가 이겼습니다.")
else:
    print("B가 이겼습니다.")
'''


'''
fruit = ['사과', '복숭아']
print(fruit)
fruit.append('귤')
print(fruit)

if '복숭아' in fruit :
    print("복숭아가 있네요^^")
if '수박'not in fruit :
    print("수박은 없네요 ㅠㅠ")
'''


'''
import random

numbers = [] #리스트 초기화 & 의미있는 변수이

for num in range(0, 10, 1): #10번반복, 0~9까지의 수 중에서 추가
    numbers.append(random.randrange(10))

print("생선된 리스트", numbers) #콤마찍어야함!!!!!!!!!!

for num in range(0, 10, 1):
    if num not in numbers:
        print("숫자 %d는(은) 리스트에 없네요."% num)
'''   



'''
number = int(input("값을 입력하세요."))
summ = 0

for i in range(0, number+1, 1):
    summ += i
    
print("1에서 %d까지의 합계: %d" % (number, summ))
'''



