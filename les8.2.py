#import random
#import random as r
#print(random.randint(0,100))
#print(r.randint(0,100))
#import random as r
#lst = [0, 1, 2 ,3 ,4 , 5, 6]
#print(r.choice(lst))
#r.shuffle(lst) #перемешать
#print(lst)

import turtle
#screen = turtle.Screen()
#t = turtle.Turtle()
#x = int(input("Введи число для одной из сторон:"))
#y = int(input("Введи поворот:"))
#z = int(input("И сколько раз?:"))
#o = int(input("Размер пера:"))
#t.pensize(o)
#while z:
  #  t.fd(x)
   # t.lt(y)
#screen.exitonclick()

screen = turtle.Screen()
t = turtle.Turtle()
t.color("purple")
t.speed(3)
t.fd(150)
t.lt(90)
t.fd(120)
t.lt(90)
t.fd(150)
t.lt(90)
t.fd(120)
t.lt(90)
t.penup()
t.speed(10)
t.goto(90, 60)
t.pendown()
t.fd(50)
t.rt(45)
t.fd(110)
t.speed(0)
t.circle(35)
t.color("blue")
t.write("Лол кек", font=("Impact",30, "normal"), align = "center")
t.shape("turtle")
t.back(90)
screen.exitonclick()