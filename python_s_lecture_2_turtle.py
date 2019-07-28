import turtle as t
import random

t.shape('turtle')


'''
t.pensize(3)
t.color('pink','purple')

figure = input("도형을 입력하시오(사각형 또는 원):")

if figure == '사각형':
    width = int(input("가로:"))
    height = int(input("세로:"))

    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)

elif figure == '원':
    radius = int(input("반지름:"))

    t.circle(radius)
    
else:
    print("잘못 입력하셨습니다.")
'''


#거북이 도장 찍기 반드시 다시해보기!!

for i in range(0, 10, 1):

    t.up()
    t.shapesize(random.randrange(7))
    t.left(random.randrange(180))
    t.goto(random.randrange(300),random.randrange(300))
    t.color(random.randrange(),random.randrange(),random.randrange())
    t.heading()
    t.stamp()
   
