#!/user/bin/python3
# coding=utf-8

from constant import *
from plane_sprite.baseSprite import BaseSprite
import random

class SupplySprite(BaseSprite):
    def __init__(self):
        image_name = './images/bomb_supply.png'
        super().__init__(image_name)
        self.speed = 2
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x) # 随机位置
    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_RECT.height:
            # 销毁方法
            self.kill()
    def __del__(self):
        pass