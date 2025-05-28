import turtle as t
import pygame
from hello_zongzi import ZongZi,play_music

t.speed(5)
t.screensize(512,512,"white")
t.pencolor("black")
t.pensize(5)
t.penup()
t.goto(100,-100)
t.pendown()

pygame.mixer.init()
music_file = "bgm.mp3"
# 先播放音乐，再开始画图
play_music(music_file)
zongzi = ZongZi()
zongzi.draw()
t.done()
pygame.mixer.music.stop()