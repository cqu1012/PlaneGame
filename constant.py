#!/user/bin/python3
# coding=utf-8
import pygame
pygame.init()
# 常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700) # 屏幕大小
GAME_NAME = "飞机大战"

CREATE_ENEMY_EVENT1 = pygame.USEREVENT + 1  # 敌机1
pygame.time.set_timer(CREATE_ENEMY_EVENT1, 200)

CREATE_ENEMY_EVENT2 = pygame.USEREVENT + 2  # 敌机2
pygame.time.set_timer(CREATE_ENEMY_EVENT2, 2000)

SHOOT_EVENT = pygame.USEREVENT + 3          # 射击事件
pygame.time.set_timer(SHOOT_EVENT, 200)

SUPPLY_EVENT = pygame.USEREVENT + 4         # 补给
pygame.time.set_timer(SUPPLY_EVENT, 10000)

WHITE = (255, 255, 255)
BLACK = (100, 100, 100)
RoyalBlue = (65,105,225)
Tomato = (255,99,71)

score_font = pygame.font.Font ("font/font.ttf", 36)
start_game_font = pygame.font.Font ("font/font.ttf", 30)
end_game_font = pygame.font.Font ("font/font.ttf", 30)
screen = pygame.display.set_mode(SCREEN_RECT.size)
clock = pygame.time.Clock()