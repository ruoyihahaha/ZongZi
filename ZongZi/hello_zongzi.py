import turtle as t
import time
import pygame

class ZongZi:
    
    def __init__(self):
        t.speed(5)
        t.screensize(512, 512, "white")
        t.pencolor("black")
        t.pensize(5)
        t.penup()
        t.goto(100, -100)
        t.pendown()
        
    #粽子主体
    def body(self):
        t.fillcolor("#82AE61")
        t.begin_fill()
        for i in range(3):
            t.circle(50,120)
            t.forward(200)
        t.end_fill()

    #粽叶纹路（左）
    def line_left(self):
        t.left(135)
        for i in range(5):
            t.penup()
            t.goto(75-i*40, -100)
            t.pendown()
            t.forward(235-i*38)

    #粽叶纹路（右）
    def line_right(self):
        t.right(90)
        for i in range(4):
            t.penup()
            t.goto(10+i*25,-25-i*25)
            t.pendown()
            t.forward(120-i*10)

    #米饭
    def rice(self):
        t.penup()
        t.goto(10,-25)
        t.pendown()
        t.fillcolor("#FFEEC8")
        t.begin_fill()
        t.forward(120)
        t.left(75)
        t.forward(102)
        t.circle(50,120)
        t.forward(95)
        t.left(75)
        t.forward(130)
        t.end_fill()

    def face(self):
        #眼睛
        t.pensize(10)
        t.penup()
        t.goto(-20,80)
        t.pendown()
        t.seth(90)
        t.forward(20)
        t.penup()
        t.goto(20,80)
        t.pendown()
        t.seth(90)
        t.forward(20)
        #嘴
        t.penup()
        t.goto(20,60)
        t.pendown()
        t.pensize(5)
        t.seth(180)
        t.fillcolor("pink")
        t.begin_fill()
        t.forward(40)
        t.seth(270)
        t.circle(20,180)
        t.end_fill()
        #米饭纹路
        t.penup()
        t.goto(20, 130)
        t.pendown()
        for i in range(2):
            t.seth(90+i*5)
            t.circle(5,180)
        t.penup()
        t.goto(-45, 35)
        t.pendown()
        for i in range(3):
            t.seth(45+i*5)
            t.circle(5,180)
        t.penup()
        t.goto(70, 60)
        t.pendown()
        for i in range(2):
            t.seth(100+i*5)
            t.circle(5,180)

    #祝福语
    def blessings(self):
        time.sleep(1.5)
        t.penup()
        t.goto(-110,250)
        t.write("你好！我是粽子！", font=("Microsoft Yahei", 24, "normal"))
        t.pendown()

        time.sleep(4)
        t.penup()
        t.goto(-65,200)
        t.pendown()
        t.write("端午安康！", font=("Microsoft Yahei", 24, "normal"))

        time.sleep(4.5)
        t.penup()
        t.goto(-155,-150)
        t.pendown()
        t.write("请问你今天有吃粽子吗？", font=("Microsoft Yahei", 24, "normal"))

        time.sleep(4.5)
        t.penup()
        t.goto(-100,-200)
        t.pendown()
        t.write("如果还没有的话", font=("Microsoft Yahei", 24, "normal"))

        time.sleep(2.5)
        t.penup()
        t.goto(-100,-250)
        t.pendown()
        t.write("请把我吃掉吧~！", font=("Microsoft Yahei", 24, "normal"))

    #画整个粽子
    def draw(self):
        self.body()
        self.line_left()
        self.line_right()
        self.rice()
        self.face()
        self.blessings()


# 定义播放BGM的函数
def play_music(music_file):
        pygame.mixer.music.load(music_file)  # 加载音乐文件
        pygame.mixer.music.play(0)  # -1表示循环播放，0为播放一次
