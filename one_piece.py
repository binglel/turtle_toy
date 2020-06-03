# -*- coding: utf-8 -*-
# 路飞骷髅
import turtle as t

# 黄底帽子
t.pu()
t.goto(0, 200)
t.circle(-130, -80)
t.pd()
t.colormode(255)
t.pensize(5)
t.color(242, 232, 184)  # 帽子黄底RGB
t.begin_fill()
t.pencolor(0, 0, 0)
t.circle(-130, 160)
t.seth(180)
t.fd(255)
t.end_fill()

# 红色线条
t.begin_fill()
t.color(221, 65, 43)  # 帽子红色带
t.pencolor(0, 0, 0)
t.seth(80)
t.circle(-130, 19)
t.seth(0)
t.fd(225)
t.seth(-59)
t.circle(-130, 19)
t.seth(180)
t.fd(255)
t.end_fill()

# 帽檐
t.begin_fill()
t.color(242, 232, 184)
t.pencolor(0, 0, 0)
t.fd(60)
t.circle(12, 180)
t.fd(375)
t.circle(12, 180)
t.fd(255 + 60)
t.end_fill()

# 脸部下半轮廓
t.pu()
t.setpos(0, -30)
t.seth(-180)
t.circle(-130, -75)
t.pd()
t.circle(-130, 150)

# 眼睛鼻子
t.pu()
t.color(33, 24, 24)  # 眼睛、鼻子RGB
t.setpos(-45, 64)
t.seth(-180)
t.pd()
t.begin_fill()
t.circle(33)
t.pu()
t.setpos(45, 64)
t.pd()
t.circle(33)
t.end_fill()

t.pu()
t.setpos(0, 5)
t.pd()
t.begin_fill()
t.circle(8)
t.end_fill()

# 下巴
t.pencolor(0, 0, 0)
t.pu()
t.setpos(0, 0)
t.seth(0)
t.circle(-75, 45)
t.pd()
t.circle(-75, 270)

# 牙齿
t.pu()
t.setpos(0, 120)
t.seth(0)
t.circle(-105, 136)
t.pd()
t.circle(-105, 86)

t.pu()
t.seth(0)
t.goto(0, 200)
t.circle(-130, 150)
t.pd()
t.circle(-130, 60)

t.pu()  # 牙齿三根竖线
t.setpos(-30, -27)
t.seth(260)
t.pd()
t.fd(52)
t.pu()
t.setpos(30, -27)
t.pd()
t.seth(-260)
t.fd(-52)
t.pu()
t.setpos(0, -30)
t.seth(-90)
t.pd()
t.fd(56)

# 上排右侧小爪爪
# 释放注释为：上排右侧小爪爪实心金方案
t.pu()
# t.color(255,215,0) #金色的RGB
t.pencolor(0, 0, 0)
t.setpos(110, 145)
t.seth(45)
t.pd()
# t.begin_fill()
t.fd(40)
t.seth(135)
t.circle(-30, 235)
t.seth(-20)
t.circle(-30, 220)
t.seth(-135)
t.fd(40)
# t.end_fill()

# 上排左侧小爪爪
t.pu()
t.pencolor(0, 0, 0)
t.setpos(-110, 145)
t.seth(135)
t.pd()
t.fd(40)
t.seth(45)
t.circle(30, 235)
t.seth(-160)
t.circle(30, 220)
t.seth(-45)
t.fd(40)

# 下排右侧小爪爪
t.pu()
t.setpos(70, -10)
t.seth(-45)
t.pd()
t.fd(70)
t.seth(45)
t.circle(-30, 235)
t.seth(-70)
t.circle(-30, 255)
t.seth(135)
t.fd(22)

# 下排左侧小爪爪
t.pu()
t.setpos(-70, -10)
t.seth(-135)
t.pd()
t.fd(70)
t.seth(135)
t.circle(30, 235)
t.seth(-110)
t.circle(30, 255)
t.seth(45)
t.fd(22)

t.done()