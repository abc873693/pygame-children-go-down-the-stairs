import pygame
import time
import colors
from pygame.locals import *


def show(text):
    print(text)


def playdied(pygame):
    pygame.mixer.music.load('music/died.mp3')
    pygame.mixer.music.play()
    time.sleep(2)
    pygame.mixer.music.stop()


def showText(DISPLAYSURF, fontObj, text, x, y):  # 抽象出一个方法用来绘制Text在屏幕上

    textSurfaceObj = fontObj.render(text, True, colors.green)  # 配置要显示的文字
    textRectObj = textSurfaceObj.get_rect()  # 获得要显示的对象的rect
    textRectObj.center = (x, y)  # 设置显示对象的坐标

    DISPLAYSURF.blit(textSurfaceObj, textRectObj)  # 绘制字体


def detectCollisions(rect1, rect2):
    (x1,y1,w1,h1) = rect1
    (x2,y2,w2,h2) = rect2
    # rect1 = (x,y,Width,Hieght)
    if (( (y1 + h1 == y2) or (y1 + h1 + 1 == y2)or (y1 + h1 - 1 == y2) ) and (x1 + w1 >= x2 and (x1 <= x2 + w2))):
        return True
    else:
        return False
