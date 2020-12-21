#!/user/bin/python3
# coding=utf-8
from constant import *
from plane_sprite import baseSprite


class BackGround(baseSprite.BaseSprite):
    def __init__(self,is_alt = False):
        image_name = './images/background.png'
        super().__init__(image_name)
        if is_alt == True:
            self.rect.y = -self.rect.height
    def update(self, *args):
        self.rect.y += self.speed
        #背景向下移动，超过边界后放到另一张的后面，实现屏幕滚动
        if self.rect.y > SCREEN_RECT.height:
            self.rect.y = -self.rect.height
