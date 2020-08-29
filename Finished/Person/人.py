from turtle import *
from time import sleep
speed(0)
def a():
    reset()
    #頭
    circle(50)
    #体
    rt(90)
    fd(100)
    lt(45)
    fd(50)
    penup()
    fd(-50)
    pendown()
    rt(90)
    fd(50)
    #腕
    penup()
    goto(0,-30)
    pendown()
    fd(50)
    penup()
    goto(0,-30)
    pendown()
    lt(90)
    fd(50)
    #顔中
    penup()
    goto(-20, 5)
    pendown()
    lt(90)
    fd(20)
    penup()
    goto(-20, 50)
    pendown()
    lt(180)
    sleep(0.5)

def b():
    reset()
    #顔
    circle(50)
    #体
    rt(90)
    fd(200)
    #
    lt(45)
    #
    #顔中
    penup()
    goto(-20, 5)
    pendown()
    lt(90)
    fd(20)
    penup()
    goto(-20, 50)
    pendown()
    lt(180)
    sleep(0.5)

while True:
    a()
    b()
