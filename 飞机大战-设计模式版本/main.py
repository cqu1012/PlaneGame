#!/user/bin/python3
# coding=utf-8
# @Author: Bot
# @Time: 2020.12.20

from constant import *
from plane_sprite.bgSprite import BackGround
from plane_sprite.enemySprite import EnemyFactory
from plane_sprite.heroSprite import Hero,SingleShoot,DoubleShoot
from plane_sprite.supplySprite import SupplySprite


class StartMenu():
    def __init__(self):
        self.__create_sprites()
    def __create_sprites(self):
        print('创建精灵')
        bg1 = BackGround()
        bg2 = BackGround(True)
        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1, bg2)  # 背景
        self.hero = Hero(SingleShoot)
        self.hero_group = pygame.sprite.Group(self.hero)  # 英雄

    def show(self):
        while True:
            clock.tick(60)     # 设置时钟
            self.__update_sprites() # 更新精灵组
            self.__event_handler()
            pygame.display.update() # 更新整个屏幕

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                PlaneGame().start_game()
            elif event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def __update_sprites(self):
        for group in [self.back_group, self.hero_group]:
            group.update()  # 更新组内所有精灵
            group.draw(screen)  # 绘制在屏幕上
        # 绘制开始游戏的字体
        welcome_text = start_game_font.render("Welcome to The Air War!", True, WHITE)
        startGame_text = start_game_font.render("Click Any Key To Start!", True, WHITE)
        screen.blit(welcome_text, (30, 200))
        screen.blit(startGame_text, (40, 300))


def sigletonDecorator(cls, *args, **kwargs):
    '''定义一个单例模式装饰器'''
    instance = {}
    def wrapperSigleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapperSigleton

@sigletonDecorator
class PlaneGame():
    def __init__(self):
        print('游戏初始化')
        pygame.display.set_caption(GAME_NAME)
        self.__create_sprites()
        self.score = 0
        pass
    def __create_sprites(self):
        print('创建精灵')
        bg1 = BackGround()
        bg2 = BackGround(True)
        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1, bg2)  # 背景
        self.enemy_group = pygame.sprite.Group()         # 敌人
        self.supply_group = pygame.sprite.Group()
        self.hero = Hero(SingleShoot)
        self.hero_group = pygame.sprite.Group(self.hero) # 英雄
        pass
    def start_game(self):
        print('开始游戏')
        while True:
            clock.tick(60)     # 设置时钟
            self.__event_handler()  # 时间监听
            self.__check_collsion() # 碰撞检测
            self.__update_sprites() # 更新精灵组
            pygame.display.update() # 更新整个屏幕


    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT1:
                self.enemy_group.add(EnemyFactory.makeEnemy('简单敌人'))
            elif event.type == CREATE_ENEMY_EVENT2:
                self.enemy_group.add(EnemyFactory.makeEnemy('中等敌人'))
            elif event.type == SHOOT_EVENT and self.hero.is_survive:
                self.hero.fire()
            elif event.type == SUPPLY_EVENT:
                self.supply_group.add(SupplySprite())
            elif not self.hero.is_survive and event.type == pygame.KEYDOWN:
                PlaneGame().__game_over()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.rect.x += self.hero.speed
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.rect.x -= self.hero.speed
        elif keys_pressed[pygame.K_UP]: # 新增上下移动
            self.hero.rect.y -= self.hero.speed
        elif keys_pressed[pygame.K_DOWN]:
            self.hero.rect.y += self.hero.speed
        else:
            self.speed = 0


    def __check_collsion(self):
        enimy_die = pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True) # 敌人死亡
        if len(enimy_die) and self.hero.is_survive:
            self.score += 10

        Hero_die = pygame.sprite.groupcollide(self.hero_group, self.enemy_group, True, False)  # 碰到敌人
        if len(Hero_die) > 0:
            self.hero.kill()
            self.hero.is_survive = False

        supply_die = pygame.sprite.groupcollide(self.hero_group, self.supply_group, False, True) # 碰到补给
        if len(supply_die) > 0:
            self.hero.shoot_mode = DoubleShoot

    def __update_sprites(self):
        for group in [self.back_group,self.hero_group, self.enemy_group, self.hero.bullets, self.supply_group]:
            group.update()          # 更新组内所有精灵
            group.draw(screen) # 绘制在屏幕上
        # 绘制得分
        if self.hero.is_survive:
            score_text = score_font.render("Score : %s" % str(self.score), True, WHITE)
            screen.blit(score_text, (10, 5))
        else:
            score_text = end_game_font.render("Your Score is %s!" % str(self.score), True, WHITE)
            exit_text = end_game_font.render("Click Any Key to Exit!", True, WHITE)
            screen.blit(score_text, (100, 200))
            screen.blit(exit_text, (60, 300))
            pass
    @staticmethod
    def __game_over():
        print('游戏结束')
        pygame.quit()
        exit()
        pass


if __name__ == '__main__':
    # game = PlaneGame()
    # game.start_game()
    control = StartMenu()
    control.show()
