from turtle import *
from time import sleep

def set_pen(x, y):
    speed(0)
    penup()
    goto(int(x), int(y))
    pendown()

def head():
    set_pen(0, 0)
    circle(50)

def head_center():
    set_pen(-20, 5)
    lt(90)
    fd(20)
    penup()
    goto(-20, 50)
    pendown()
    lt(180)
    sleep(0.5)

def body():
    set_pen(0, 0)
    rt(90)
    fd(100)

def bou():
    set_pen(0, -100)
    fd(100)

def ude_ashi():
    #足
    set_pen(0, -100)
    lt(45)
    fd(50)
    fd(-50)
    rt(90)
    fd(50)
    fd(-50)
    #腕
    set_pen(0,-30)
    fd(50)
    set_pen(0,-30)
    lt(90)
    fd(50)

page=0
while True:
    set_pen(0, 0)
    head()
    body()
    if page==1:
        page=0
        bou()
    elif page==0:
        page=1
        ude_ashi()
    head_center()
    reset()