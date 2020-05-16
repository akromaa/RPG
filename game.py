# coding:utf-8
import pygame
from Player import *


class Game():
    def __init__(self):
        self.pressed = {}
        self.hero = Player(self, "images/perso_nu.png", (750, 600), pygame.K_DOWN)
        self.squellette = Player(self,"images/squellette.png", (600, 400), pygame.K_DOWN)
        self.all_player = pygame.sprite.Group()


    def check_collision(self, sprite, group):
        return  pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def player_list(self):
        self.all_player.add(self.hero)# ajout du hero dans le groupe de sprite all_player