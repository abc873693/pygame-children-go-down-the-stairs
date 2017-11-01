import pygame,random
from pygame.locals import *


class Character(pygame.sprite.Sprite):

    defualt = 0
    left = 1
    right = 2
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

    def load(self):
        self.master_image = pygame.image.load(
            "images/player.png").convert_alpha()
        self.frame_width = 32
        self.frame_height = 32
        self.rect = 0, 0, self.frame_width, self.frame_height
        self.image_rect = self.master_image.get_rect()

    def update(self, status):
        frame_x = self.frame_width * Character.rect_defualt[0]
        frame_y = 0
        if(status == Character.defualt):
            frame_y = 0
        if(status == Character.left):
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            frame_x = self.frame_width * \
                (Character.rect_left[0] - self.frame // 4)
            frame_y = Character.rect_left[1]
            self.image_rect.centerx -= 2
        if(status == Character.right):
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            frame_x = self.frame_width * \
                (Character.rect_right[0] + self.frame // 4)
            frame_y = self.frame_height * Character.rect_right[1]
            self.image_rect.centerx += 2
        rect = (frame_x, frame_y, self.frame_width, self.frame_height)
        self.image = self.master_image.subsurface(rect)

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

    def load(self,x,y):
        self.master_image = pygame.image.load(
            "images/normal.png").convert_alpha()
        self.frame_width = 97
        self.frame_height = 16
        self.image_rect = x, y, self.frame_width, self.frame_height
        self.rect = self.master_image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.image = self.master_image

    def update(self,width,height):
        self.rect.centery += 1
        if self.rect.centery >= height:
            self.rect.centerx = random.randrange(30, width-30)
            self.rect.centery = 8
        #self.master_image.get_rect().centery -= 1
        #if (self.master_image.get_rect().centery < 0):
        #     self.master_image.get_rect().centery = -1 * self.frame_height
