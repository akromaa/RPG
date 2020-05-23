# coding:utf-8
import pygame
from Player import *
from dialogue import *


class Game():
    def __init__(self):
        self.pressed = {}
        self.hero = Player(self, "images/perso_nu.png", (750, 600), pygame.K_DOWN)
        self.squellette = Player(self,"images/squellette.png", (600, 400), pygame.K_DOWN)

        self.all_player = pygame.sprite.Group()
        self.all_pnj = pygame.sprite.Group()


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def pnj(self):
        self.all_pnj.add(self.squellette)# création de groupe de pnj pour les gestion de collissions ajouter tout les pnj
        # memo  for perso in pnj.sprites(): if perso == squellette: .....

    def player_list(self):
        self.all_player.add(self.hero)# ajout du hero dans le groupe de sprite all_player


    def dialogue(self):
        print(self.all_pnj)
        print(self.all_player)
        if pygame.sprite.groupcollide(self.all_player, self.all_pnj, False, False):
            print (texte1)


