#!/user/bin/python3
# coding=utf-8
from constant import *

'''
游戏的基础精灵
'''

from abc import ABCMeta, abstractmethod
class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed = 1):
        super().__init__() #父类方法初始化
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
    @abstractmethod
    def update(self, *args):
        # 默认在垂直方向上移动
        # self.rect.y += self.speed
        pass