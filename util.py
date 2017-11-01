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
    
def showText(DISPLAYSURF,fontObj,text,x,y):#抽象出一个方法用来绘制Text在屏幕上

    textSurfaceObj = fontObj.render(text, True, colors.green)# 配置要显示的文字
    textRectObj = textSurfaceObj.get_rect()# 获得要显示的对象的rect
    textRectObj.center = (x, y)# 设置显示对象的坐标

    DISPLAYSURF.blit(textSurfaceObj, textRectObj)# 绘制字体