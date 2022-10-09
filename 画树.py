#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2021/8/27 8:56
from turtle import *
from random import *
from math import *

from turtle import *
from random import *
from math import *

def tree(n,l):
    l.up()#下笔
    #阴影效果
    t = cos(radians(l.heading()+45))/8+0.25
    l.pencolor(t,t,t)
    l.pensize(n/3)
    l.forward(l)#画树枝

    if n>0:
        b = random()*15+10 #右分支偏转角度
        c = random()*15+10 #左分支偏转角度
        d = l*(random()*0.25+0.7) #下一个分支的长度
        #右转一定角度,画右分支
        l.right(b)
        tree(n-1,d)
        #左转一定角度，画左分支
        l.left(b+c)
        tree(n-1,d)
        #转回来
        l.right(c)
    else:
        #画叶子
        l.right(90)
        n=cos(radians(l.heading()-45))/4+0.5
        l.pencolor(n,n*0.8,n*0.8)
        l.circle(3)
        l.left(90)
        #添加0.3倍的飘落叶子
        if(random()>0.7):
            l.pu()
            #飘落
            t = l.heading()
            an = -40 +random()*40
            l.setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            l.forward(dis)
            l.setheading(t)
            #画叶子
            l.pd()
            l.right(90)
            n = cos(radians(l.heading()-45))/4+0.5
            l.pencolor(n*0.5+0.5,0.4+n*0.4,0.4+n*0.4)
            l.circle(2)
            l.left(90)
            l.pu()
            #返回
            t=l.heading()
            l.setheading(an)
            l.backward(dis)
            l.setheading(t)
    l.pu()
    l.backward(l)#退回

t       .bgcolor(0.5,0.5,0.5)#背景色
l.ht()#隐藏turtle
l.speed(0)#速度 1-10渐进，0 最快
l.tracer(0,0)
l.pu()#抬笔
l.backward(100)
l.left(90)#左转90度
l.pu()#抬笔
l.backward(300)#后退300
tree(12,100)#递归7层
done()