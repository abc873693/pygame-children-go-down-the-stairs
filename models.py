import pygame
import random
from pygame.locals import *


class Character(pygame.sprite.Sprite):

    #key state
    defualt = 0
    left = 1
    right = 2
    #Character state
    died = -1
    drop = 0
    onFloor = 1
    # player frame location
    rect_defualt = (8, 0)
    rect_left = (3, 0)
    rect_right = (0, 1)

    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)
        self.target_surface = target
        self.image = None
        self.master_image = None
        self.rect = None
        self.topleft = 0, 0
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 1
        self.last_frame = 15
        self.last_time = 0
        self.state = Character.drop

    def load(self, x=300, y=50):
        self.master_image = pygame.image.load(
            "images/player.png").convert_alpha()
        self.frame_width = 32
        self.frame_height = 32
        self.rect = x, y, self.frame_width, self.frame_height
        self.image_rect = self.master_image.get_rect()
        self.image_rect.centerx = x
        self.image_rect.centery = y
        self.image_rect[2] = 32
        self.image_rect[3] = 32

    def update(self, state_key):
        frame_x = self.frame_width * Character.rect_defualt[0]
        frame_y = 0
        if(state_key == Character.defualt):
            frame_y = 0
        if(state_key == Character.left):
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            frame_x = self.frame_width * \
                (Character.rect_left[0] - self.frame // 4)
            frame_y = Character.rect_left[1]
            if(self.image_rect.centerx>=16):
                self.image_rect.centerx -= 2
        if(state_key == Character.right):
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            frame_x = self.frame_width * \
                (Character.rect_right[0] + self.frame // 4)
            frame_y = self.frame_height * Character.rect_right[1]
            if(self.image_rect.centerx <= 386):
                self.image_rect.centerx += 2
        rect = (frame_x, frame_y, self.frame_width, self.frame_height)
        self.image = self.master_image.subsurface(rect)
        if(self.state == Character.drop):
            self.image_rect.centery += 2
        elif (self.state == Character.onFloor):
            self.image_rect.centery -= 1

    def draw(self, surface):
        surface.blit(self.image, (self.image_rect[0], self.image_rect[1]))


class Floor(pygame.sprite.Sprite):
    default = 0

    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)
        self.target_surface = target
        self.image = None
        self.master_image = None
        self.rect = None
        self.topleft = 0, 0
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0

    def load(self, x, y):
        self.master_image = pygame.image.load(
            "images/normal.png").convert_alpha()
        self.frame_width = 97
        self.frame_height = 16
        self.image_rect = x, y, self.frame_width, self.frame_height
        self.rect = self.master_image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.image = self.master_image

    def update(self, width, height):
        self.rect.centery -= 1
        if self.rect.centery <= 0:
            self.rect.centerx = random.randrange(30, width - 30)
            self.rect.centery = 396
        #self.master_image.get_rect().centery -= 1
        # if (self.master_image.get_rect().centery < 0):
        #     self.master_image.get_rect().centery = -1 * self.frame_height
