import util
import models
import pygame,random
import colors
from pygame.locals import *



mWidth = 400
mHeight = 400
pygame.init()
screen = pygame.display.set_mode((mWidth, mHeight), 0, 32)
pygame.display.set_caption("Sprite 精靈類別測試：one cat")
framerate = pygame.time.Clock()

all_floor = pygame.sprite.Group()

character = models.Character(screen)
character.load()

for i in range(5):
  floor = models.Floor(screen)
  floor_x = random.randrange(30, mWidth-30)
  floor_y = i * 80 
  floor.load(floor_x,floor_y)
  all_floor.add(floor)


# floor = models.Floor(screen)
# floor.load("images/sprite.png", 200, 100, 4)
# group.add(floor)

state_character = 0
gameLoop = True
while gameLoop:
    for event in pygame.event.get():
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
    screen.fill(colors.black)
    character.update(state_character)
    character.draw(screen)
    #group.update(state_character)
    #group.draw(screen)
    #floor.update(mWidth,mHeight)
    #floor.draw(screen)
    
    # for item in group.sprites():
    #     if type(item) == models.Character:
    #         models.Character(item).update(ticks)
    #     if type(item) == models.Floor:
    #         models.Floor(item).update(ticks)
    
    all_floor.update(mWidth,mHeight)
    all_floor.draw(screen)
    pygame.display.update()
    framerate.tick(80)
pygame.quit()