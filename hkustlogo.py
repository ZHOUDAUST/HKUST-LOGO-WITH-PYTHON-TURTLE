#=*- coding: utf-8 -*-

"""
@topic
@creatde on Tue Sep 10 19:56:00
@author zhouda

"""
import random
from turtle import *

def main():

    s = Screen()
    s.screensize(bg = "wheat")
    t = Turtle()
    t.speed(5)
    t.up(); t.goto(0,100); t.down()
    #打印位置
    print(t.pos())
    
    ##头##
    t.color("yellow")
    t.begin_fill(); t.circle(50); t.end_fill()
    
    #打印坐标
    print(t.pos())

    ##书托##
    t.up(); t.goto(0,70); t.down()
    t.color("blue","blue")
    t.begin_fill()
    t.up(); t.goto(20,90); t.down()
    t.setheading(180); t.circle(20,90)
    t.up(); t.goto(20,90); t.down(); t.lt(90)
    t.fd(95)
    t.rt(60); t.fd(36); print(t.pos())
    t.rt(120); t.fd(85)
    #画第二个圆
    t.circle(25,65)
    #拼接
    t.rt(65); t.fd(25.34);print(t.pos())
    #左半边
    t.up(); t.goto(-0,70); t.down()
    t.setheading(90);t.circle(20,90)
    t.fd(95);
    t.lt(60); t.fd(36)
    t.lt(120); t.fd(85)
    t.circle(-25,65)
    t.goto(-0,44.39)
    t.end_fill()

    ##权杖##
    t.color("yellow","yellow")
    t.begin_fill()
    t.up(); t.goto(25.34,34.39); t.down()
    t.setheading(-90); t.fd(150)
    t.lt(30); t.fd(100)
    t.setheading(180); t.fd(150.68)
    t.rt(120); t.fd(100)
    t.setheading(90); t.fd(150)
    t.rt(90); t.fd(15)
    t.rt(90); t.fd(150)
    t.rt(30); t.fd(70)
    t.setheading(0); t.fd(90.68)
    t.lt(120); t.fd(70)
    t.setheading(90); t.fd(150)
    t.setheading(0); t.fd(15)
    t.end_fill()

    ##右手臂##
    t.color("blue","blue")
    t.begin_fill()
    t.up(); t.goto(113,43.82); t.down()
    t.setheading(-90); t.fd(130)
    #画弧
    t.circle(-120,47)
    t.setheading(120); t.fd(20)
    t.rt(60); t.circle(100,47); t.goto(93,43.82)
    t.setheading(0); t.fd(20)
    t.end_fill()

    t.begin_fill()
    t.up(); t.goto(80,43.82); t.down()
    t.setheading(-90); t.fd(128)
    #画弧
    t.circle(-87,47)
    t.rt(90); t.fd(20)
    t.rt(90); t.circle(67,47); t.goto(60,43.82)
    t.setheading(0); t.fd(20)
    t.end_fill()
    
    #t.up()
    
    
main()
