import util
import models
import pygame
import random
import time
import colors
from pygame.locals import *


mWidth = 400
mHeight = 400
pygame.init()
pygame.mixer.init()  # 運行之前需要初始化
screen = pygame.display.set_mode((mWidth, mHeight), 0, 32)
pygame.display.set_caption("小朋友下樓梯")
framerate = pygame.time.Clock()
font = pygame.font.Font("fonts/msjh.ttf", 24)

counts = 0  # 初始化计时器
COUNT = pygame.USEREVENT + 1  # 自定义计时事件
pygame.time.set_timer(COUNT, 1500)  # 每隔1.5秒发送一次自定义事件


all_floor = pygame.sprite.Group()

character = models.Character(screen)
character.load()

for i in range(5):
    floor = models.Floor(screen)
    floor_x = random.randrange(30, mWidth - 30)
    floor_y = i * 80
    floor.load(floor_x, floor_y)
    all_floor.add(floor)


# floor = models.Floor(screen)
# floor.load("images/sprite.png", 200, 100, 4)
# group.add(floor)

state_character = 0
gameLoop = True
game_state = True
while gameLoop:
    for event in pygame.event.get():
        if event.type == COUNT:
            counts = counts + 1
        if event.type == pygame.QUIT:
            gameLoop = False
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                state_character = models.Character.left
            if (event.key == pygame.K_RIGHT):
                state_character = models.Character.right
            if (event.key == pygame.K_UP):
                moveY = -4
            if (event.key == pygame.K_DOWN):
                moveY = 4
        elif (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT):
                state_character = models.Character.defualt
            if (event.key == pygame.K_RIGHT):
                state_character = models.Character.defualt
            if (event.key == pygame.K_UP):
                state_character = models.Character.defualt
            if (event.key == pygame.K_DOWN):
                state_character = models.Character.defualt
    
    if(character.state != character.died):
      flag = False
      for item in all_floor.sprites():
        if(util.detectCollisions(character.image_rect,item.rect)):
          flag = True
        print(character.image_rect,' ',item.rect)
      if(flag):
        character.state = character.onFloor
      else:
        character.state = character.drop
      print(character.state) 
      print('-----------------------------------')
      screen.fill(colors.black)
      character.update(state_character)
      character.draw(screen)

      all_floor.update(mWidth, mHeight)
      all_floor.draw(screen)

      text = "層數"
      util.showText(screen, font, text, 360, 15)
      countstext = str(counts)
      util.showText(screen, font, countstext, 360, 50)
      pygame.display.update()

    framerate.tick(80)
    if(character.image_rect[1] >= mHeight and game_state):
      character.state = character.died
      util.playdied(pygame)
      character.update(state_character)
      game_state = False
pygame.quit()

# for item in group.sprites():
    #     if type(item) == models.Character:
    #         models.Character(item).update(ticks)
    #     if type(item) == models.Floor:
    #         models.Floor(item).update(ticks)