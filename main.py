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

group = pygame.sprite.Group()
character = models.Character(screen)
character.load()
group.add(character)

floor_x = random.randrange(0, mWidth)
floor_y = mHeight
floor = models.Floor(screen)
floor.load(floor_x,floor_y)


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
    floor.update()
    floor.draw(screen)
    
    # for item in group.sprites():
    #     if type(item) == models.Character:
    #         models.Character(item).update(ticks)
    #     if type(item) == models.Floor:
    #         models.Floor(item).update(ticks)
    pygame.display.update()
    framerate.tick(50)
pygame.quit()