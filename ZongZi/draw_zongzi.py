import turtle as t
import pygame
from hello_zongzi import ZongZi,play_music

#初始化音乐
pygame.mixer.init()
music_file = "bgm.mp3"
# 先播放音乐，再开始画图
play_music(music_file)

zongzi = ZongZi()
zongzi.draw()

t.done()
pygame.mixer.music.stop()
