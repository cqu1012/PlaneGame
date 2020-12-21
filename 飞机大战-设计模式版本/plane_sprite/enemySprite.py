#!/user/bin/python3
# coding=utf-8
from constant import *
from plane_sprite.baseSprite import BaseSprite
import random

class BaseEnemy(BaseSprite):
    def __init__(self, image_name, health_point = 1):
        super().__init__(image_name)
        self.score = 10                        # 分数
        self.health_point = health_point       # 生命值
        self.speed = random.randint(3, 6)      # 随机的速度
        self.rect.bottom = 0                   # 从底部出现
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x) # 随机位置
    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_RECT.height:
            # 销毁方法
            self.kill()


class Enemy1(BaseEnemy):
    def __init__(self):
        image_name = './images/enemy1.png'
        health_point = 1
        super().__init__(image_name, health_point)


class Enemy2(BaseEnemy):
    def __init__(self):
        self.score = 30
        image_name = './images/enemy2.png'
        health_point = 5
        super().__init__(image_name, health_point)

class EnemyFactory():
    @staticmethod
    def makeEnemy(enemyType):
        if enemyType == '简单敌人':
            enemy = Enemy1()
        elif enemyType == '中等敌人':
            enemy = Enemy2()
        else:
            raise ValueError('不支持的参数：%s' % enemyType)
        return enemy
