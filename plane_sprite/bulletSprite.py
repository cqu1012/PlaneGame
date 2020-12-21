#!/user/bin/python3
# coding=utf-8
# import pygame
from plane_sprite.baseSprite import BaseSprite
class Bullte(BaseSprite):
    def __init__(self):
        image_name = './images/bullet1.png'
        super().__init__(image_name)  # 父类方法初始化
        self.speed = -10
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
