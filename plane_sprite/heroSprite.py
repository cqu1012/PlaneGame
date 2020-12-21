#!/user/bin/python3
# coding=utf-8
from constant import *
from abc import abstractmethod
from plane_sprite.baseSprite import BaseSprite
from plane_sprite.bulletSprite import Bullte

def sigletonDecorator(cls, *args, **kwargs):
    '''定义一个单例模式装饰器'''
    instance = {}
    def wrapperSigleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapperSigleton

@sigletonDecorator
class Hero(BaseSprite):
    def __init__(self, shoot_mode):
        image_name = './images/me1.png'
        super().__init__(image_name)
        self.speed = 10
        # SCREEN_RECT.centerx, SCREEN_RECT.bottom - 180
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.y = SCREEN_RECT.bottom - 180
        self.bullets = pygame.sprite.Group()
        self.shoot_mode = shoot_mode
        self.is_survive = True
        pass
    def update(self):
        # 边界控制
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        pass
    def fire(self):
        # 调用外部的开火方式
        self.shoot_mode(self).fire()



class BaseShoot():
    def __init__(self, hero):
        self.hero = hero
        pass
    @abstractmethod
    def fire(self):
        pass

class SingleShoot(BaseShoot):
    def fire(self):
        bullet = Bullte()
        bullet.rect.bottom = self.hero.rect.y - 20
        bullet.rect.centerx = self.hero.rect.centerx
        self.hero.bullets.add(bullet)

class DoubleShoot(BaseShoot):
    def fire(self):
        for i in range(1, 3):
            bullet = Bullte()
            bullet.rect.bottom = self.hero.rect.y - 20
            bullet.rect.centerx = self.hero.rect.centerx + ((-1) ** i) * 20
            self.hero.bullets.add(bullet)


