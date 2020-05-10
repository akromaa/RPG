# coding:utf-8
import pygame
from Player import *


class Game():
    def __init__(self):
        self.pressed = {}
        self.hero = Player(self, "images/perso_nu.png", (750, 600), pygame.K_DOWN)
        self.squellette = Player(self,"images/squellette.png", (600, 400), pygame.K_DOWN)
    # forgeron = Player("images/forgeron.png", (200, 700), pygame.K_RIGHT)
    # blue_bird = Player("images/blue_bird.png", (400,400), pygame.K_DOWN)

    def check_collision(self, sprite, group):
        return  pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)
