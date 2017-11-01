
import pygame,time
import colors
from pygame.locals import *


# 定义几个颜色


def showText(DISPLAYSURF,fontObj,text,x,y):#抽象出一个方法用来绘制Text在屏幕上

    textSurfaceObj = fontObj.render(text, True, colors.green)# 配置要显示的文字
    textRectObj = textSurfaceObj.get_rect()# 获得要显示的对象的rect
    textRectObj.center = (x, y)# 设置显示对象的坐标

    DISPLAYSURF.blit(textSurfaceObj, textRectObj)# 绘制字体

